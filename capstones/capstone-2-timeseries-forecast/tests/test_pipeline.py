"""Train -> backtest -> predict on synthetic data, asserting shapes and scores."""

from __future__ import annotations

import json

import numpy as np
import pytest

from forecast.metrics import evaluate, mae, mape, rmse
from forecast.models import BaselineModel, NaiveSeasonalModel, build_model
from forecast.pipeline import rolling_origin_backtest, train_pipeline
from forecast.predict import forecast, load_model


def test_metrics_perfect_prediction():
    y = np.array([1.0, 2.0, 3.0])
    assert mae(y, y) == 0.0
    assert rmse(y, y) == 0.0
    assert mape(y, y) == 0.0


def test_baseline_fit_predict_shapes(synthetic_series):
    model = BaselineModel(season_length=7, conf_level=0.9).fit(synthetic_series)
    res = model.predict(14)
    assert len(res) == 14
    assert res.yhat.shape == (14,)
    assert (res.yhat_lower <= res.yhat).all()
    assert (res.yhat <= res.yhat_upper).all()
    # future dates strictly after history
    assert res.index[0] > synthetic_series.index[-1]


def test_naive_seasonal_repeats_last_season(synthetic_series):
    model = NaiveSeasonalModel(season_length=7).fit(synthetic_series)
    res = model.predict(7)
    last_week = synthetic_series.to_numpy()[-7:]
    np.testing.assert_allclose(res.yhat, last_week)


def test_build_model_unknown_raises():
    with pytest.raises(ValueError):
        build_model("does-not-exist")


def test_optional_models_fall_back_to_baseline(synthetic_series):
    # sarima/prophet/lstm should not raise even without their deps installed.
    for name in ("sarima", "prophet", "lstm"):
        model = build_model(name).fit(synthetic_series)
        res = model.predict(5)
        assert len(res) == 5
        assert np.isfinite(res.yhat).all()


def test_backtest_returns_metrics(synthetic_series):
    bt = rolling_origin_backtest(
        synthetic_series,
        model_name="baseline",
        season_length=7,
        conf_level=0.9,
        horizon=14,
        folds=2,
    )
    assert bt["folds"] >= 1
    for key in ("mae", "rmse", "mape"):
        assert np.isfinite(bt[key])


def test_baseline_captures_trend(synthetic_series):
    """The trend-aware baseline must beat a flat mean-only forecast in-sample,
    proving it actually models the upward drift (not just the level)."""
    import numpy as np

    base = build_model("baseline").fit(synthetic_series)
    y = synthetic_series.to_numpy()
    h = len(y)
    t = np.arange(h, dtype=float)
    base_fitted = base._slope * t + base._intercept + np.array(
        [base._seasonal[i % base.season_length] for i in range(h)]
    )
    base_mae = evaluate(y, base_fitted)["mae"]
    mean_mae = evaluate(y, np.full(h, y.mean()))["mae"]
    assert base._slope > 0  # detected the upward trend
    assert base_mae < mean_mae


def test_train_pipeline_saves_artifact(settings):
    result = train_pipeline(settings, save=True)
    assert result.artifact_path is not None
    assert result.artifact_path.exists()
    assert (settings.resolved_model_dir() / "latest.joblib").exists()
    meta = json.loads((settings.resolved_model_dir() / "latest.json").read_text())
    assert meta["model_name"] == "baseline"
    assert meta["n_observations"] > 0
    for key in ("mae", "rmse", "mape"):
        assert np.isfinite(result.metrics[key])


def test_predict_after_train(settings):
    train_pipeline(settings, save=True)
    model, meta = load_model(settings)
    points = forecast(10, settings=settings, model=model)
    assert len(points) == 10
    first = points[0]
    assert set(first) == {"date", "yhat", "yhat_lower", "yhat_upper"}
    assert first["yhat_lower"] <= first["yhat"] <= first["yhat_upper"]


def test_forecast_trains_when_no_artifact(settings):
    # No artifact saved yet -> load_model trains a baseline transparently.
    points = forecast(5, settings=settings)
    assert len(points) == 5

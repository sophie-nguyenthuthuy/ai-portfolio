"""Pluggable forecasting models.

All models implement the :class:`ForecastModel` interface:

    fit(series) -> self
    predict(horizon) -> ForecastResult   # yhat + lower/upper bands

Base-dep models (numpy / scikit-learn only):
    * ``BaselineModel``        seasonal-naive + linear trend (default for tests)
    * ``NaiveSeasonalModel``   pure seasonal naive

Optional-dep models (lazily imported, graceful fallback to BaselineModel):
    * ``SarimaModel``   statsmodels SARIMAX
    * ``ProphetModel``  prophet
    * ``LSTMModel``     torch
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable

import numpy as np
import pandas as pd

from .logging_conf import get_logger

log = get_logger(__name__)


@dataclass
class ForecastResult:
    """Forecast output aligned to future dates."""

    index: pd.DatetimeIndex
    yhat: np.ndarray
    yhat_lower: np.ndarray
    yhat_upper: np.ndarray

    def __len__(self) -> int:
        return len(self.yhat)


@runtime_checkable
class ForecastModel(Protocol):
    name: str

    def fit(self, series: pd.Series) -> "ForecastModel": ...

    def predict(self, horizon: int) -> ForecastResult: ...


def _future_index(series: pd.Series, horizon: int) -> pd.DatetimeIndex:
    freq = series.index.freq or pd.infer_freq(series.index) or "D"
    start = series.index[-1] + pd.tseries.frequencies.to_offset(freq)
    return pd.date_range(start=start, periods=horizon, freq=freq)


# z-score lookup without scipy (keeps deps light).
_Z = {0.80: 1.2816, 0.90: 1.6449, 0.95: 1.9600, 0.975: 2.2414, 0.99: 2.5758}


def _z_for(conf_level: float) -> float:
    if conf_level in _Z:
        return _Z[conf_level]
    # nearest tabulated level
    nearest = min(_Z, key=lambda k: abs(k - conf_level))
    return _Z[nearest]


def _prediction_bands(
    yhat: np.ndarray, residual_std: float, conf_level: float, horizon: int
) -> tuple[np.ndarray, np.ndarray]:
    z = _z_for(conf_level)
    # widen the band with the forecast horizon (uncertainty grows over time).
    growth = np.sqrt(np.arange(1, horizon + 1))
    margin = z * max(residual_std, 1e-9) * growth
    return yhat - margin, yhat + margin


class _FittableBase:
    """Shared fit bookkeeping for numpy-based models."""

    name = "base"

    def __init__(self, season_length: int = 7, conf_level: float = 0.9) -> None:
        self.season_length = int(season_length)
        self.conf_level = float(conf_level)
        self._series: pd.Series | None = None
        self._residual_std: float = 1.0

    def _require_fit(self) -> pd.Series:
        if self._series is None:
            raise RuntimeError(f"{self.name} model is not fitted")
        return self._series


class NaiveSeasonalModel(_FittableBase):
    """Forecast each future day as the value from one season ago."""

    name = "naive_seasonal"

    def fit(self, series: pd.Series) -> "NaiveSeasonalModel":
        self._series = series.astype(float)
        m = self.season_length
        if len(series) > m:
            in_sample = series.shift(m).bfill()
            self._residual_std = float(np.std(series.to_numpy() - in_sample.to_numpy()))
        return self

    def predict(self, horizon: int) -> ForecastResult:
        series = self._require_fit()
        m = self.season_length
        history = series.to_numpy()
        last_season = history[-m:] if len(history) >= m else np.resize(history, m)
        yhat = np.array([last_season[i % m] for i in range(horizon)], dtype=float)
        lower, upper = _prediction_bands(yhat, self._residual_std, self.conf_level, horizon)
        return ForecastResult(_future_index(series, horizon), yhat, lower, upper)


class BaselineModel(_FittableBase):
    """Seasonal-naive component + a linear trend fit with least squares.

    Default model used in unit tests — pure numpy, no optional deps. Decomposes
    the series into a linear trend (OLS on the time index) and per-season-position
    average residuals, then projects both forward.
    """

    name = "baseline"

    def fit(self, series: pd.Series) -> "BaselineModel":
        self._series = series.astype(float)
        y = series.to_numpy(dtype=float)
        n = len(y)
        t = np.arange(n, dtype=float)

        # OLS linear trend.
        A = np.vstack([t, np.ones_like(t)]).T
        self._slope, self._intercept = np.linalg.lstsq(A, y, rcond=None)[0]
        trend = self._slope * t + self._intercept

        # Seasonal profile from detrended residuals.
        detrended = y - trend
        m = self.season_length
        profile = np.zeros(m, dtype=float)
        for pos in range(m):
            members = detrended[pos::m]
            profile[pos] = members.mean() if len(members) else 0.0
        self._seasonal = profile
        self._n = n

        fitted = trend + np.array([profile[i % m] for i in range(n)])
        self._residual_std = float(np.std(y - fitted)) or 1.0
        return self

    def predict(self, horizon: int) -> ForecastResult:
        series = self._require_fit()
        m = self.season_length
        future_t = np.arange(self._n, self._n + horizon, dtype=float)
        trend = self._slope * future_t + self._intercept
        seasonal = np.array([self._seasonal[(self._n + i) % m] for i in range(horizon)])
        yhat = trend + seasonal
        lower, upper = _prediction_bands(yhat, self._residual_std, self.conf_level, horizon)
        return ForecastResult(_future_index(series, horizon), yhat, lower, upper)


class SarimaModel(_FittableBase):
    """SARIMAX from statsmodels (optional dep). Falls back to BaselineModel."""

    name = "sarima"

    def __init__(
        self,
        season_length: int = 7,
        conf_level: float = 0.9,
        order: tuple[int, int, int] = (1, 1, 1),
        seasonal_order: tuple[int, int, int, int] | None = None,
    ) -> None:
        super().__init__(season_length, conf_level)
        self.order = order
        self.seasonal_order = seasonal_order or (1, 0, 1, season_length)
        self._impl = None
        self._fallback: BaselineModel | None = None

    def fit(self, series: pd.Series) -> "SarimaModel":
        self._series = series.astype(float)
        try:
            from statsmodels.tsa.statespace.sarimax import SARIMAX  # type: ignore

            model = SARIMAX(
                series.to_numpy(dtype=float),
                order=self.order,
                seasonal_order=self.seasonal_order,
                enforce_stationarity=False,
                enforce_invertibility=False,
            )
            self._impl = model.fit(disp=False)
            log.info("fitted SARIMAX%s x %s", self.order, self.seasonal_order)
        except Exception as exc:  # missing dep OR convergence failure
            log.warning("SARIMA unavailable (%s) — falling back to baseline", exc)
            self._fallback = BaselineModel(self.season_length, self.conf_level).fit(series)
        return self

    def predict(self, horizon: int) -> ForecastResult:
        series = self._require_fit()
        if self._impl is None:
            assert self._fallback is not None
            return self._fallback.predict(horizon)
        fc = self._impl.get_forecast(steps=horizon)
        yhat = np.asarray(fc.predicted_mean, dtype=float)
        ci = fc.conf_int(alpha=1 - self.conf_level)
        ci = np.asarray(ci, dtype=float)
        lower, upper = ci[:, 0], ci[:, 1]
        return ForecastResult(_future_index(series, horizon), yhat, lower, upper)


class ProphetModel(_FittableBase):
    """Facebook Prophet (optional dep). Falls back to BaselineModel."""

    name = "prophet"

    def fit(self, series: pd.Series) -> "ProphetModel":
        self._series = series.astype(float)
        self._impl = None
        self._fallback = None
        try:
            from prophet import Prophet  # type: ignore

            df = pd.DataFrame({"ds": series.index, "y": series.to_numpy(dtype=float)})
            model = Prophet(
                interval_width=self.conf_level,
                weekly_seasonality=True,
                yearly_seasonality=True,
                daily_seasonality=False,
            )
            model.fit(df)
            self._impl = model
            log.info("fitted Prophet")
        except Exception as exc:
            log.warning("Prophet unavailable (%s) — falling back to baseline", exc)
            self._fallback = BaselineModel(self.season_length, self.conf_level).fit(series)
        return self

    def predict(self, horizon: int) -> ForecastResult:
        series = self._require_fit()
        if self._impl is None:
            assert self._fallback is not None
            return self._fallback.predict(horizon)
        future = self._impl.make_future_dataframe(periods=horizon, freq="D")
        fc = self._impl.predict(future).tail(horizon)
        return ForecastResult(
            pd.DatetimeIndex(fc["ds"].to_numpy()),
            fc["yhat"].to_numpy(dtype=float),
            fc["yhat_lower"].to_numpy(dtype=float),
            fc["yhat_upper"].to_numpy(dtype=float),
        )


class LSTMModel(_FittableBase):
    """Small LSTM (optional torch dep). Falls back to BaselineModel."""

    name = "lstm"

    def __init__(
        self,
        season_length: int = 7,
        conf_level: float = 0.9,
        lookback: int = 28,
        hidden: int = 16,
        epochs: int = 50,
    ) -> None:
        super().__init__(season_length, conf_level)
        self.lookback = lookback
        self.hidden = hidden
        self.epochs = epochs
        self._impl = None
        self._fallback: BaselineModel | None = None

    def fit(self, series: pd.Series) -> "LSTMModel":
        self._series = series.astype(float)
        try:
            import torch  # type: ignore
            from torch import nn  # type: ignore

            y = series.to_numpy(dtype=float)
            self._mean, self._std = float(y.mean()), float(y.std() or 1.0)
            z = (y - self._mean) / self._std

            xs, ys = [], []
            for i in range(len(z) - self.lookback):
                xs.append(z[i : i + self.lookback])
                ys.append(z[i + self.lookback])
            if not xs:
                raise ValueError("series too short for LSTM lookback")
            X = torch.tensor(np.array(xs), dtype=torch.float32).unsqueeze(-1)
            Y = torch.tensor(np.array(ys), dtype=torch.float32).unsqueeze(-1)

            class _Net(nn.Module):
                def __init__(self, hidden: int) -> None:
                    super().__init__()
                    self.lstm = nn.LSTM(1, hidden, batch_first=True)
                    self.head = nn.Linear(hidden, 1)

                def forward(self, x):  # noqa: ANN001
                    out, _ = self.lstm(x)
                    return self.head(out[:, -1, :])

            net = _Net(self.hidden)
            opt = torch.optim.Adam(net.parameters(), lr=0.01)
            loss_fn = nn.MSELoss()
            net.train()
            for _ in range(self.epochs):
                opt.zero_grad()
                loss = loss_fn(net(X), Y)
                loss.backward()
                opt.step()
            net.eval()
            with torch.no_grad():
                resid = (net(X).squeeze(-1).numpy() - Y.squeeze(-1).numpy()) * self._std
            self._residual_std = float(np.std(resid)) or 1.0
            self._impl = net
            self._torch = torch
            log.info("fitted LSTM (lookback=%d, hidden=%d)", self.lookback, self.hidden)
        except Exception as exc:
            log.warning("LSTM unavailable (%s) — falling back to baseline", exc)
            self._fallback = BaselineModel(self.season_length, self.conf_level).fit(series)
        return self

    def predict(self, horizon: int) -> ForecastResult:
        series = self._require_fit()
        if self._impl is None:
            assert self._fallback is not None
            return self._fallback.predict(horizon)
        torch = self._torch
        y = series.to_numpy(dtype=float)
        z = list((y[-self.lookback :] - self._mean) / self._std)
        preds = []
        self._impl.eval()
        with torch.no_grad():
            for _ in range(horizon):
                x = torch.tensor(np.array(z[-self.lookback :]), dtype=torch.float32).reshape(1, -1, 1)
                nxt = float(self._impl(x).item())
                preds.append(nxt)
                z.append(nxt)
        yhat = np.array(preds) * self._std + self._mean
        lower, upper = _prediction_bands(yhat, self._residual_std, self.conf_level, horizon)
        return ForecastResult(_future_index(series, horizon), yhat, lower, upper)


_REGISTRY: dict[str, type] = {
    "baseline": BaselineModel,
    "naive_seasonal": NaiveSeasonalModel,
    "sarima": SarimaModel,
    "prophet": ProphetModel,
    "lstm": LSTMModel,
}


def available_models() -> list[str]:
    return sorted(_REGISTRY)


def build_model(name: str, *, season_length: int = 7, conf_level: float = 0.9) -> ForecastModel:
    """Factory. Unknown names raise; optional-dep models degrade at fit time."""
    key = (name or "baseline").lower()
    if key not in _REGISTRY:
        raise ValueError(f"unknown model '{name}'. choices: {available_models()}")
    return _REGISTRY[key](season_length=season_length, conf_level=conf_level)

terraform {
  required_version = ">= 1.6.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# Local Docker provider — validate-able without cloud credentials.
provider "docker" {}

resource "docker_image" "forecast_api" {
  name         = var.image_name
  keep_locally = true
}

resource "docker_container" "forecast_api" {
  name  = "${var.project_name}-api"
  image = docker_image.forecast_api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  env = [
    "FORECAST_MODEL_NAME=${var.model_name}",
    "FORECAST_USE_MLFLOW=false",
  ]

  restart = "unless-stopped"

  healthcheck {
    test     = ["CMD", "curl", "-fsS", "http://localhost:8000/health"]
    interval = "30s"
    timeout  = "5s"
    retries  = 3
  }
}

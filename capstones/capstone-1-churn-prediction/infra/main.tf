# Terraform skeleton for the churn-prediction service.
# Validate-only: `terraform init -backend=false && terraform validate`.
# No real cloud resources are applied here.

terraform {
  required_version = ">= 1.6.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "churn_api" {
  name = var.image_name
}

resource "docker_container" "churn_api" {
  name  = "${var.project_name}-api"
  image = docker_image.churn_api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  env = [
    "CHURN_LOG_LEVEL=INFO",
    "CHURN_CLASSIFIER=${var.classifier}",
  ]
}

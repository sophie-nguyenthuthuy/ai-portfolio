# Terraform skeleton for the MLOps platform (local Docker provider).
# Validate-only: `terraform init -backend=false && terraform validate`.
# No real cloud resources are applied here — this models the api + mlflow stack.

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

resource "docker_network" "mlops" {
  name = "${var.project_name}-net"
}

resource "docker_image" "api" {
  name = var.image_name
}

resource "docker_container" "api" {
  name  = "${var.project_name}-api"
  image = docker_image.api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  networks_advanced {
    name = docker_network.mlops.name
  }

  env = [
    "MLOPS_LOG_LEVEL=INFO",
    "MLOPS_CLASSIFIER=${var.classifier}",
    "MLOPS_REGISTRY_BACKEND=${var.registry_backend}",
  ]
}

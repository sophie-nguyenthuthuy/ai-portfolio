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

# Local container image for the API service. A real deployment would swap this
# for a cloud module (ECS/Cloud Run/AKS); the skeleton stays validate-able with
# no credentials and no apply required.
resource "docker_image" "api" {
  name         = "${var.image_name}:${var.image_tag}"
  keep_locally = true
}

resource "docker_container" "api" {
  name  = var.service_name
  image = docker_image.api.image_id

  ports {
    internal = 8000
    external = var.host_port
  }

  env = [
    "VISION_BACKEND=dummy",
    "VISION_OCR_ENGINE=stub",
    "VISION_USE_MLFLOW=false",
  ]

  restart = "unless-stopped"
}

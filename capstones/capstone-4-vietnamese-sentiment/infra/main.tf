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

# Local container deployment of the sentiment API. A real environment would
# swap this for a cloud module (ECS/Cloud Run/AKS); kept provider-pinned and
# validate-able with no apply required.
resource "docker_image" "nlpvi_api" {
  name         = var.image_name
  keep_locally = true
}

resource "docker_container" "nlpvi_api" {
  name  = "nlpvi-api"
  image = docker_image.nlpvi_api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  env = [
    "NLPVI_MODEL_BACKEND=sklearn",
    "NLPVI_MLFLOW_ENABLED=false",
  ]

  restart = "unless-stopped"
}

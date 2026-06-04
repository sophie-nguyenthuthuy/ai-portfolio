# Terraform skeleton for the rag-chatbot service.
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

resource "docker_image" "rag_api" {
  name = var.image_name
}

resource "docker_container" "rag_api" {
  name  = "${var.project_name}-api"
  image = docker_image.rag_api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  env = [
    "RAGBOT_LOG_LEVEL=INFO",
    "RAGBOT_EMBEDDER=${var.embedder}",
    "RAGBOT_VECTOR_STORE=${var.vector_store}",
    "RAGBOT_LLM=${var.llm}",
  ]
}

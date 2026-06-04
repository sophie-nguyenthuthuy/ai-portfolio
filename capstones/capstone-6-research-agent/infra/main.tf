# Terraform skeleton for the research-agent service.
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

resource "docker_image" "agent_api" {
  name = var.image_name
}

resource "docker_container" "agent_api" {
  name  = "${var.project_name}-api"
  image = docker_image.agent_api.image_id

  ports {
    internal = 8000
    external = var.api_port
  }

  env = [
    "AGENT_LOG_LEVEL=INFO",
    "AGENT_LLM_BACKEND=${var.llm_backend}",
    "AGENT_GRAPH_BACKEND=${var.graph_backend}",
  ]
}

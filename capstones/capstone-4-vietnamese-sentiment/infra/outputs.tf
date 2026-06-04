output "api_container_name" {
  description = "Name of the running API container"
  value       = docker_container.nlpvi_api.name
}

output "api_url" {
  description = "Base URL of the sentiment API"
  value       = "http://localhost:${var.api_port}"
}

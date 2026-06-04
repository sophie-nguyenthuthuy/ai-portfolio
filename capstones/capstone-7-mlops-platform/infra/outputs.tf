output "container_name" {
  description = "Name of the running API container."
  value       = docker_container.api.name
}

output "network_name" {
  description = "Docker network the stack runs on."
  value       = docker_network.mlops.name
}

output "api_url" {
  description = "Base URL of the MLOps platform API."
  value       = "http://localhost:${var.api_port}"
}

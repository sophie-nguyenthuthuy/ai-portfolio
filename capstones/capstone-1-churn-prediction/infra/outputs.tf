output "container_name" {
  description = "Name of the running API container."
  value       = docker_container.churn_api.name
}

output "api_url" {
  description = "Base URL of the churn prediction API."
  value       = "http://localhost:${var.api_port}"
}

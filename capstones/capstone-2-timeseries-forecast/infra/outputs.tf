output "container_name" {
  description = "Name of the running API container."
  value       = docker_container.forecast_api.name
}

output "api_endpoint" {
  description = "Local URL for the forecasting API."
  value       = "http://localhost:${var.api_port}"
}

output "image_id" {
  description = "Resolved Docker image id."
  value       = docker_image.forecast_api.image_id
}

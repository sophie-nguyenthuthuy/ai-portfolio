output "service_name" {
  description = "Deployed container name."
  value       = docker_container.api.name
}

output "api_endpoint" {
  description = "Base URL for the running API."
  value       = "http://localhost:${var.host_port}"
}

output "image_ref" {
  description = "Image reference used for the deployment."
  value       = "${var.image_name}:${var.image_tag}"
}

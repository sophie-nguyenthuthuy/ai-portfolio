output "container_name" {
  description = "Name of the running API container."
  value       = docker_container.agent_api.name
}

output "api_url" {
  description = "Base URL of the research-agent API."
  value       = "http://localhost:${var.api_port}"
}

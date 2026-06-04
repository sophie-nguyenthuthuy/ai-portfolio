output "container_name" {
  description = "Name of the running API container."
  value       = docker_container.rag_api.name
}

output "api_url" {
  description = "Base URL of the RAG chatbot API."
  value       = "http://localhost:${var.api_port}"
}

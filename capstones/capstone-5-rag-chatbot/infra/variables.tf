variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "capstone-rag"
}

variable "image_name" {
  description = "Container image to deploy."
  type        = string
  default     = "capstone-rag:latest"
}

variable "api_port" {
  description = "Host port mapped to the API container."
  type        = number
  default     = 8000
}

variable "embedder" {
  description = "Embedding backend (hashing | sentence-transformers)."
  type        = string
  default     = "hashing"
}

variable "vector_store" {
  description = "Vector store backend (memory | qdrant)."
  type        = string
  default     = "memory"
}

variable "llm" {
  description = "LLM backend (fake | ollama)."
  type        = string
  default     = "fake"
}

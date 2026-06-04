variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "capstone-research-agent"
}

variable "image_name" {
  description = "Container image to deploy."
  type        = string
  default     = "capstone-research-agent:latest"
}

variable "api_port" {
  description = "Host port mapped to the API container."
  type        = number
  default     = 8000
}

variable "llm_backend" {
  description = "LLM backend used by the agent (fake | ollama)."
  type        = string
  default     = "fake"
}

variable "graph_backend" {
  description = "Graph backend (auto | langgraph | simple)."
  type        = string
  default     = "auto"
}

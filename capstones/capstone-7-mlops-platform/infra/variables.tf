variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "capstone-mlops"
}

variable "image_name" {
  description = "Container image to deploy."
  type        = string
  default     = "capstone-mlops:latest"
}

variable "api_port" {
  description = "Host port mapped to the API container."
  type        = number
  default     = 8000
}

variable "classifier" {
  description = "Reference model family used by the service."
  type        = string
  default     = "gradient_boosting"
}

variable "registry_backend" {
  description = "Model registry backend: local | mlflow."
  type        = string
  default     = "local"
}

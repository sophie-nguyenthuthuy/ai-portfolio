variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "capstone-churn"
}

variable "image_name" {
  description = "Container image to deploy."
  type        = string
  default     = "capstone-churn:latest"
}

variable "api_port" {
  description = "Host port mapped to the API container."
  type        = number
  default     = 8000
}

variable "classifier" {
  description = "Model family used by the service."
  type        = string
  default     = "gradient_boosting"
}

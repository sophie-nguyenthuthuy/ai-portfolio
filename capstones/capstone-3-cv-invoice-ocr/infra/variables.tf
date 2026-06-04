variable "service_name" {
  description = "Container / service name."
  type        = string
  default     = "cv-invoice-ocr"
}

variable "image_name" {
  description = "Docker image repository name."
  type        = string
  default     = "capstone-3-cv-invoice-ocr"
}

variable "image_tag" {
  description = "Docker image tag to deploy."
  type        = string
  default     = "latest"
}

variable "host_port" {
  description = "Host port mapped to the container's 8000."
  type        = number
  default     = 8000
}

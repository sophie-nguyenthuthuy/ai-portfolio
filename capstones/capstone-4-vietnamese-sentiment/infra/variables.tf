variable "image_name" {
  description = "Container image for the sentiment API"
  type        = string
  default     = "capstone-4-vietnamese-sentiment:latest"
}

variable "api_port" {
  description = "Host port to expose the API on"
  type        = number
  default     = 8000
}

variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "timeseries-forecast"
}

variable "image_name" {
  description = "Container image to deploy."
  type        = string
  default     = "capstone-2-timeseries-forecast:latest"
}

variable "api_port" {
  description = "Host port mapped to the API container."
  type        = number
  default     = 8000
}

variable "model_name" {
  description = "Default forecasting model."
  type        = string
  default     = "baseline"
}

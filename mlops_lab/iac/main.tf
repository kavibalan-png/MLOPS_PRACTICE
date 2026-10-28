provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "model_bucket" {
  bucket = "mlops-lab-model-artifacts"
}

resource "aws_instance" "model_server" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.small"
  tags = { Name = "ml-model-server" }
}

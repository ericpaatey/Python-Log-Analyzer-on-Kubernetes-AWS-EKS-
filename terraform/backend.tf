terraform {

  backend "s3" {

    bucket         = "devops-build-lab-terraform-state"
    key            = "eks/log-analyzer/terraform.tfstate"
    region         = "us-east-1"

    dynamodb_table = "terraform-lock-table"

    encrypt = true
  }
}
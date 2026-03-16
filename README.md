# DevOps Build Lab – Python Log Analyzer on Kubernetes (AWS EKS)

(A fully automated cloud-native deployment of a Python Log Analyzer API running on Kubernetes using AWS EKS, Terraform, Docker, and GitHub Actions.)

This project demonstrates a modern DevOps workflow with Infrastructure as Code, CI/CD automation, containerization, and Kubernetes orchestration.

---

## Architecture Overview

The application is deployed using a fully automated pipeline:

Developer Push → GitHub → CI/CD → Docker → Amazon ECR → Terraform → AWS EKS → Kubernetes Pods → ALB → Users

### Key Components

- **Terraform** – Infrastructure provisioning
- **GitHub Actions** – CI/CD pipeline
- **Docker** – Containerized Python application
- **Amazon ECR** – Container registry
- **Amazon EKS** – Kubernetes cluster
- **Amazon RDS (PostgreSQL)** – Database for storing log results
- **Application Load Balancer (ALB)** – External traffic routing
- **Amazon CloudWatch** – Logging and monitoring
- **S3 Remote State + DynamoDB Locking** – Terraform state management

---

## Architecture Diagram

![Automated EKS Deployment](architecture/diagram.png)

---

## Application Overview

The **Python Log Analyzer API** processes log files and extracts useful insights such as:

- Error frequency
- Top IP addresses
- Status code distribution
- Suspicious activity patterns

Example endpoint:

POST /analyze


Input:

{
"log": "ERROR: database connection failed"
}


Output:

{
"errors_detected": 1,
"severity": "high"
}


---

## Infrastructure Provisioning (Terraform)

Terraform provisions the following AWS resources:

- VPC and networking
- Amazon EKS cluster
- IAM roles and policies
- Amazon RDS PostgreSQL database
- Application Load Balancer
- Security groups
- CloudWatch (for monitoring & Observability)

### Terraform Backend

Remote state management:

- **Amazon S3** – Terraform state storage
- **DynamoDB** – State locking

Example:

terraform {

backend "s3" {

bucket = "devops-build-lab-terraform-state"

key = "eks/terraform.tfstate"

region = "us-east-1"

dynamodb_table = "terraform-locks"

}

}


---

## CI/CD Pipeline

The CI/CD pipeline is implemented using **GitHub Actions**.

Pipeline steps:

1. Code pushed to GitHub
2. Build Docker image
3. Push image to Amazon ECR
4. Run Terraform apply
5. Deploy application to Kubernetes

Example workflow:

name: Deploy to EKS

  on:
  push:
  branches:

  main

  jobs:
  deploy:
  runs-on: ubuntu-latest

  steps:

    name: Checkout
    uses: actions/checkout@v3

    name: Build Docker Image
    run: docker build -t log-analyzer .

    name: Push to ECR
    run: echo "Push image step"

  name: Terraform Apply
  run: terraform apply -auto-approve
  
---

## Kubernetes Deployment

The application is deployed using Kubernetes manifests.

### Deployment

kubectl apply -f k8s/deployment.yaml


### Service
kubectl apply -f k8s/service.yaml

### Ingress
kubectl apply -f k8s/ingress.yaml


---

## Traffic Flow

User → Application Load Balancer → Kubernetes Ingress → Service → Pods → PostgreSQL Database

---

## Monitoring and Observability

Application and cluster monitoring are handled using:

- **Amazon CloudWatch Logs**
- Container logs from EKS
- ALB access logs

This allows tracking:

- API request logs
- Kubernetes pod logs
- infrastructure metrics

---

## Running Locally

Clone the repository:

git clone https://github.com/ericpaatey/python-log-analyzer-on-kubernetes-aws-esks-.git

cd devops-build-lab-log-analyzer


Build the container:

docker build -t log-analyzer .


Run locally:

docker run -p 5000:5000 log-analyzer


---

## Future Improvements

Possible enhancements:

- Horizontal Pod Autoscaling (HPA)
- Prometheus + Grafana monitoring
- Kubernetes Helm charts
- Blue/Green deployments
- ArgoCD GitOps deployment model

---

## Key DevOps Concepts Demonstrated

- Infrastructure as Code
- Kubernetes container orchestration
- CI/CD automation
- Immutable infrastructure
- Cloud-native application deployment
- Observability and monitoring

---

## Author

I built this project as part of my **DevOps Build Lab**, a series of my hands-on cloud engineering projects focused on real-world infrastructure automation.


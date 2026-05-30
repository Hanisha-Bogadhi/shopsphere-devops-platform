# ShopSphere – End-to-End DevOps CI/CD Microservices Platform on AWS

## Project Overview

ShopSphere is a microservices-based e-commerce platform built to demonstrate modern DevOps practices, cloud deployment, CI/CD automation, containerization, monitoring, and production-style application delivery.

The platform consists of multiple Dockerized services deployed on AWS EC2 using Docker Compose. The complete workflow includes source control with GitHub, automated CI/CD using GitHub Actions, container image management through Docker Hub, reverse proxying using Nginx, and monitoring with Prometheus, Grafana, and cAdvisor.

---

## Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions CI/CD
    │
    ▼
Docker Hub Registry
    │
    ▼
AWS EC2 Instance
    │
    ▼
Docker Compose
    │
    ▼
Nginx Reverse Proxy
    │
    ├────────────► Frontend Service
    │
    ├────────────► Product Service
    │
    └────────────► Cart Service
    │
    ▼
Prometheus + Grafana + cAdvisor
```

---

## Technology Stack

### Cloud
- AWS EC2

### CI/CD
- GitHub Actions

### Containerization
- Docker
- Docker Compose

### Reverse Proxy
- Nginx

### Monitoring & Observability
- Prometheus
- Grafana
- cAdvisor

### Application Services
- Frontend
- Product Service
- Cart Service

### Version Control
- Git
- GitHub

---

## Microservices

### Frontend
Provides the user interface for browsing products and interacting with the application.

### Product Service
Handles product catalog data and product-related API requests.

### Cart Service
Handles cart operations and cart-related API requests.

### Nginx Reverse Proxy
Routes incoming requests to the appropriate backend services.

### Routing

```text
/            → Frontend
/products    → Product Service
/cart        → Cart Service
```

---

## Features

- Microservices architecture
- Docker containerization
- Docker Compose orchestration
- Nginx reverse proxy routing
- GitHub Actions CI/CD pipeline
- Docker Hub integration
- AWS EC2 deployment
- Prometheus monitoring
- Grafana dashboards
- cAdvisor container metrics
- Production-style deployment workflow
- Infrastructure automation practices

---

## Repository Structure

```text
shopsphere-devops-platform/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── frontend/
│
├── product-service/
│
├── cart-service/
│
├── nginx/
│   └── default.conf
│
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
│
├── docker-compose.yml
├── docker-compose.local.yml
├── screenshots/
└── README.md
```

---

# Local Deployment

## Clone Repository

```bash
git clone https://github.com/Hanisha-Bogadhi/shopsphere-devops-platform.git

cd shopsphere-devops-platform
```

## Start Application

```bash
docker compose -f docker-compose.local.yml up -d
```

## Verify Running Containers

```bash
docker ps
```

## Local URLs

### Frontend

```text
http://localhost
```

### Grafana

```text
http://localhost:3000
```

### Prometheus

```text
http://localhost:9090
```

### cAdvisor

```text
http://localhost:8081
```

---

# Production Deployment

Application images are built and pushed to Docker Hub.

Production deployment is performed on AWS EC2 using Docker Compose.

## Pull Latest Images

```bash
docker compose pull
```

## Deploy Containers

```bash
docker compose up -d
```

## Verify Running Containers

```bash
docker ps
```

---

# Production Verification

After deployment, obtain the EC2 Public IPv4 address from the AWS Console.

## Verify Frontend

Open in browser:

```text
http://<EC2-PUBLIC-IP>
```

Example:

```text
http://13.235.xxx.xxx
```

Expected Result:
- ShopSphere frontend loads successfully.
- Product catalog is visible.
- Navigation between services works correctly.

---

## Verify Product Service

Open:

```text
http://<EC2-PUBLIC-IP>/products
```

Expected Result:
- Product Service responds successfully.

---

## Verify Cart Service

Open:

```text
http://<EC2-PUBLIC-IP>/cart
```

Expected Result:
- Cart Service responds successfully.

---

## Verify Grafana

Open:

```text
http://<EC2-PUBLIC-IP>:3000
```

Default Login:

```text
Username: admin
Password: admin
```

Expected Result:
- Grafana dashboard opens successfully.

---

## Verify Prometheus

Open:

```text
http://<EC2-PUBLIC-IP>:9090
```

Expected Result:
- Prometheus UI loads.
- Targets are healthy.

---

## Verify cAdvisor

Open:

```text
http://<EC2-PUBLIC-IP>:8081
```

Expected Result:
- Container metrics are displayed.

---

# CI/CD Pipeline

## Workflow

```text
Developer Pushes Code
            │
            ▼
GitHub Repository
            │
            ▼
GitHub Actions Pipeline
            │
            ▼
Build Docker Images
            │
            ▼
Push Images to Docker Hub
            │
            ▼
Deploy to AWS EC2
            │
            ▼
Verify Application Availability
```

## CI/CD Stages

1. Source Code Checkout
2. Docker Build
3. Docker Hub Authentication
4. Image Push to Docker Hub
5. EC2 Deployment
6. Container Health Verification

---

# Monitoring & Observability

## Prometheus

Collects application and infrastructure metrics.

### Metrics Monitored

- Container CPU Usage
- Container Memory Usage
- Container Network Usage
- Container Disk Usage
- Service Availability
- Docker Container Health

---

## Grafana

Provides dashboards and visualizations for monitoring system performance and application health.

### Dashboard Examples

- CPU Utilization
- Memory Utilization
- Container Statistics
- Service Availability
- Resource Consumption

---

## cAdvisor

Collects container-level metrics from Docker and exposes them to Prometheus.

### Metrics Available

- CPU Usage
- Memory Usage
- Filesystem Usage
- Network Usage
- Container Health

---

# Key DevOps Concepts Demonstrated

- Continuous Integration (CI)
- Continuous Deployment (CD)
- Docker Containerization
- Docker Compose Orchestration
- Reverse Proxy Configuration
- Cloud Deployment
- Monitoring and Observability
- Infrastructure Automation
- Image Registry Management
- Microservices Architecture
- Production Deployment Practices

---

# Challenges Solved During Development

- Multi-container service communication
- Nginx reverse proxy routing
- Docker networking issues
- Container volume mounting issues
- Prometheus configuration troubleshooting
- Grafana datasource integration
- CI/CD pipeline automation
- AWS deployment validation
- Service health monitoring

---

# Future Enhancements

- Kubernetes Deployment
- Helm Charts
- AWS EKS
- Auto Scaling
- Load Balancer Integration
- Blue-Green Deployments
- Canary Releases
- Terraform Infrastructure Provisioning
- SSL/TLS with Let's Encrypt
- Custom Domain Integration

---


# Author

**Hanisha Bogadhi**

DevOps Engineer | AWS Cloud | Docker | CI/CD | Monitoring | Linux | GitHub Actions
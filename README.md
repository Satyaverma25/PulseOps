# 🚀 Sensor Monitoring & Observability Dashboard

A complete DevOps + Observability project built using **Python, Docker, Kubernetes, Prometheus, and Grafana**.

This project monitors a sensor service in real-time and visualizes system metrics such as:

* CPU Usage
* Memory Usage
* Latency
* Request Count
* Service Health Status

The application is containerized using Docker and deployed on Kubernetes with full observability using Prometheus and Grafana.

---

# 📌 Project Overview

This project demonstrates how modern DevOps monitoring systems work in real-world environments.

The sensor service exposes custom metrics which are scraped by Prometheus and visualized using Grafana dashboards.

The frontend dashboard provides a clean UI to display live monitoring information.

---

# 🛠️ Tech Stack

## Backend

* Python
* Flask
* Prometheus Client Library

## DevOps & Monitoring

* Docker
* Kubernetes
* Minikube
* Prometheus
* Grafana
* kubectl

## Frontend

* HTML
* CSS
* JavaScript

---

# 📂 Project Structure

```bash
.
├── Dockerfile
├── docker-compose.yml
├── deployment.yaml
├── service.yaml
├── prometheus.yml
├── sensor_service.py
├── README.md
├── screenshots/
└── performance-budget-report.md
```

---

# ⚙️ Features

✅ Real-time CPU monitoring
✅ Real-time memory monitoring
✅ Request latency tracking
✅ Prometheus metrics scraping
✅ Grafana dashboards
✅ Kubernetes deployment
✅ Docker containerization
✅ NodePort service exposure
✅ Live observability system

---

# 📊 Monitoring Metrics

The following custom Prometheus metrics are used:

| Metric                  | Description                 |
| ----------------------- | --------------------------- |
| `cpu_usage_percent`     | CPU usage of sensor service |
| `memory_usage_percent`  | Memory consumption          |
| `sensor_requests_total` | Total API requests          |
| `up`                    | Service health status       |

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t sensor-app .
```

## Run Container

```bash
docker run -p 8000:8000 sensor-app
```

---

# ☸️ Kubernetes Deployment

## Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

## Apply Service

```bash
kubectl apply -f service.yaml
```

## Verify Pods

```bash
kubectl get pods
```

## Verify Services

```bash
kubectl get svc
```

---

# 📈 Prometheus Setup

## Port Forward Prometheus

```bash
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090
```

## Access Prometheus

```bash
http://localhost:9090
```

### Sample Queries

```promql
up
```

```promql
cpu_usage_percent
```

```promql
memory_usage_percent
```

```promql
sensor_requests_total
```

---

# 📉 Grafana Setup

## Port Forward Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

## Access Grafana

```bash
http://localhost:3000
```

---

# 🖥️ Dashboard Preview

## Sensor Monitoring Dashboard

* CPU Usage
* Memory Usage
* Latency
* Service Status

## Grafana Observability Dashboard

* Request monitoring
* CPU graphs
* Memory graphs
* Real-time metrics visualization

---

# 📷 Screenshots

## Application Dashboard

<img width="100%" src="screenshots/Screenshot 2025-12-24 195124.png">

## Prometheus Metrics

<img width="100%" src="screenshots/Screenshot 2025-12-24 195159.png">

## Grafana Dashboard

<img width="100%" src="screenshots/Screenshot 2025-12-24 195249.png">

---

# 🔥 How It Works

1. Sensor service generates metrics.
2. Prometheus scrapes metrics periodically.
3. Grafana reads data from Prometheus.
4. Dashboards visualize system performance.
5. Kubernetes manages deployment and scaling.

---

# 🧠 Learning Outcomes

Through this project, I learned:

* Docker containerization
* Kubernetes deployments and services
* Prometheus monitoring
* Grafana dashboard creation
* Observability concepts
* Infrastructure monitoring
* DevOps workflow
* Metrics collection and visualization

---

# 🚀 Future Improvements

* Add alerting system using Alertmanager
* Add CI/CD pipeline using Jenkins/GitHub Actions
* Add authentication and security
* Deploy on cloud platforms (AWS/GCP/Azure)
* Add logging using ELK Stack
* Add auto-scaling in Kubernetes

---

# 👨‍💻 Author

## Satya Prakash

B.Tech CSE Student
Lovely Professional University
DevOps | Cloud |

GitHub: [https://github.com/Satyaverma25](https://github.com/Satyaverma25)

---

# 🌟 Final Result

This project successfully demonstrates a complete DevOps observability pipeline using Kubernetes, Prometheus, and Grafana with live monitoring dashboards.

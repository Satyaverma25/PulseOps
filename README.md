# DevOps Edge Observability Project

## Overview
This project showcases my work on optimizing a Python-based sensor service and building a lightweight observability stack designed for edge and resource-constrained environments.

The primary objective was to reduce CPU and memory usage, stabilize metrics collection, and ensure reliable observability using industry-standard tools while staying within a strict memory limit.

---

## Problem Statement
The original Python sensor service suffered from multiple performance and observability issues:

- The `/metrics` endpoint performed heavy computations on every scrape
- High CPU utilization under load
- Excessive memory consumption
- Prometheus scrape delays and timeouts
- Intermittent Grafana dashboard failures

These issues made the service unsuitable for edge deployments where system resources are limited.

---

## Solution Approach
I followed a structured optimization and observability approach:

- Identified CPU and memory bottlenecks in the Python service
- Refactored the `/metrics` endpoint to keep it lightweight
- Exposed only essential Prometheus metrics
- Used proper Prometheus exposition standards
- Removed unnecessary computations from the metrics path
- Containerized all components using Docker
- Orchestrated the stack using Docker Compose
- Built minimal Grafana dashboards for clear visibility

This resulted in a stable and resource-efficient observability setup.

---

## Observability Stack
The following tools were used:

- **Python** – Optimized sensor service
- **Prometheus** – Metrics scraping and storage
- **Grafana** – Metrics visualization
- **Docker & Docker Compose** – Containerization and orchestration

The stack was intentionally kept simple to support edge use cases.

---

## Custom Metrics
The service exposes the following custom metrics:

- **sensor_requests_total**  
  Tracks the total number of requests handled by the service.

- **sensor_processing_latency_seconds**  
  Measures request processing latency.

- **sensor_cpu_spike**  
  Simulates CPU spike behavior to observe system stress.

These metrics help analyze system performance and resource behavior.

---

## Performance Results
Memory usage was monitored using `docker stats`.

| Component        | Approx Memory Usage |
|------------------|---------------------|
| Sensor Service   | ~27 MB              |
| Prometheus       | ~28 MB              |
| Grafana          | ~120 MB             |
| **Total**        | **~175 MB**         |

The complete observability stack runs well within the **300 MB memory constraint**, making it suitable for edge environments.

---

## Screenshots
The `screenshots/` directory contains:

- Grafana dashboard
- Prometheus targets showing service status (UP)
- Docker stats displaying memory usage

---

## Video Walkthrough
A complete project walkthrough is available here:  
https://drive.google.com/file/d/1ktwZh1qrbiHeYdMdZniLZlVYo2REiPwb/view?usp=drive_link

---

## How to Run the Project

Make sure Docker and Docker Compose are installed.

```bash
docker compose up --build

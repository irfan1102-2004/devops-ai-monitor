# 🚀 DevOps AI Monitor

An AI-powered DevOps monitoring platform that collects system metrics and application logs, analyzes infrastructure health, and presents actionable insights through a modern web dashboard.

The project combines **FastAPI, React, PostgreSQL, Docker, Prometheus, Loki, Grafana, and AI-powered analysis** into a full-stack DevOps monitoring solution.

## 🌐 Live Demo

**Frontend:**
https://devops-ai-monitor-frontend.onrender.com

**Backend API:**
https://devops-ai-monitor.onrender.com

> The production deployment uses a graceful fallback when Prometheus and Loki are not available in the cloud environment. The complete monitoring stack remains available for local Docker-based development.

---

## ✨ Features

* 📊 System health monitoring
* 🖥️ CPU and memory utilization monitoring
* 📈 Prometheus-based infrastructure metrics
* 📋 Loki-based application log collection
* 🤖 AI-powered system health analysis
* 🚨 Health alerts and recommendations
* 🔍 Recent error and warning analysis
* 🖥️ Interactive React dashboard
* 🔌 RESTful APIs using FastAPI
* 🗄️ PostgreSQL database integration
* 🐳 Docker and Docker Compose support
* 📡 Grafana monitoring dashboard
* 🔄 GitHub Actions CI/CD pipeline
* ☁️ Production deployment on Render
* 🛡️ Graceful fallback when cloud monitoring services are unavailable

---

## 🏗️ Architecture

### Local Development

```text
                    ┌──────────────────┐
                    │   React Frontend │
                    │     Dashboard    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    └───────┬───┬──────┘
                            │   │
              ┌─────────────┘   └──────────────┐
              ▼                                ▼
       ┌──────────────┐                 ┌──────────────┐
       │  Prometheus  │                 │     Loki     │
       └──────┬───────┘                 └──────┬───────┘
              │                                │
              ▼                                ▼
       ┌──────────────┐                 ┌──────────────┐
       │ Node Exporter│                 │   Promtail   │
       └──────────────┘                 └──────────────┘

                    ┌──────────────────┐
                    │    PostgreSQL    │
                    └──────────────────┘

                    ┌──────────────────┐
                    │     Grafana      │
                    └──────────────────┘
```

### Production Deployment

```text
┌──────────────────┐
│   React Frontend │
│     on Render    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  FastAPI Backend │
│     on Render    │
└───────┬───┬──────┘
        │   │
        │   └──────────────► PostgreSQL
        │
        ├────────► Prometheus unavailable
        │             ↓
        │       Graceful fallback
        │
        └────────► Loki unavailable
                      ↓
                Graceful fallback
```

The production backend does not depend on Prometheus or Loki being available. Their URLs are configurable through environment variables, allowing the application to operate safely in environments where the monitoring stack is not deployed.

---

## 🤖 AI Monitoring

The AI analysis component evaluates the available infrastructure and log information and generates:

* System health status
* CPU utilization analysis
* Memory utilization analysis
* Monitoring alerts
* Error and warning counts
* Recent error and warning logs
* Operational recommendations

When live monitoring services are unavailable, the analyzer returns a **`LIMITED`** health state instead of causing an API failure.

Example:

```json
{
  "system_health": "LIMITED",
  "cpu_usage_percent": 0.0,
  "memory_usage_percent": 0.0,
  "alerts": [
    "Live system metrics are unavailable.",
    "Live log monitoring is unavailable."
  ]
}
```

This prevents monitoring-service failures from crashing the application or frontend.

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* Alembic

### Frontend

* React
* Vite
* Node.js
* Axios

### Database

* PostgreSQL

### Monitoring

* Prometheus
* Node Exporter
* Loki
* Promtail
* Grafana

### DevOps

* Docker
* Docker Compose
* Git
* GitHub Actions

### Cloud

* Render

---

## 📁 Project Structure

```text
devops-ai-monitor/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── core/
│   │   └── models/
│   ├── alembic/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── monitoring/
├── docs/
├── screenshots/
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🐳 Running Locally

### Prerequisites

Make sure the following are installed:

* Docker Desktop
* Git
* Python 3.10+
* Node.js

### Clone the repository

```bash
git clone https://github.com/irfan1102-2004/devops-ai-monitor.git
cd devops-ai-monitor
```

### Start the monitoring stack

```bash
docker compose -f backend/docker-compose.yml up -d
```

This starts the local services including:

* FastAPI backend
* PostgreSQL
* Prometheus
* Node Exporter
* Loki
* Promtail
* Grafana

### Access local services

```text
Backend:
http://localhost:8000

Prometheus:
http://localhost:9090

Grafana:
http://localhost:3000
```

The frontend can be started separately using the project's frontend configuration.

---

## 🔄 CI/CD

GitHub Actions is used to automatically validate the project.

The CI pipeline includes:

* Backend testing
* Frontend build verification
* Docker build verification

The project is also connected to Render for cloud deployment.

```text
Git Push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Validation
   ↓
Render Deployment
   ↓
Production
```

---

## ☁️ Production Deployment

The application is deployed using Render.

### Production services

* React frontend
* FastAPI backend
* PostgreSQL database

The production environment uses configurable monitoring service URLs.

If Prometheus or Loki are unavailable, the backend gracefully falls back to a `LIMITED` monitoring state instead of returning an HTTP 500 error.

This allows the application to remain available without requiring additional cloud monitoring infrastructure.

---

## 📸 Dashboard

### Production Dashboard

*Add screenshots of the working dashboard here.*

```text
screenshots/
├── dashboard.png
├── ai-analysis.png
└── monitoring.png
```

---

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

* Full-stack application development
* REST API development
* Database integration
* Containerization
* Infrastructure monitoring
* Centralized logging
* AI-assisted system analysis
* CI/CD
* Cloud deployment
* Production debugging
* Failure handling and graceful degradation

---

## 🚀 Future Improvements

Potential future enhancements include:

* Deploying Prometheus and Loki to a dedicated cloud environment
* Real-time WebSocket monitoring
* Advanced anomaly detection
* Historical performance analytics
* Email/Slack alerting
* Kubernetes deployment
* Infrastructure-as-Code using Terraform
* Advanced AI-powered incident diagnosis

---

## 📌 Project Status

**Production deployment complete. ✅**

The application is available as a live portfolio project and continues to support local development with the complete Docker-based monitoring stack.

---

## 📄 License

This project is licensed under the MIT License.

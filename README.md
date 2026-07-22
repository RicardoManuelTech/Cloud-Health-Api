# Cloud Health API

A production-ready Flask REST API demonstrating health monitoring, readiness checks, metrics, structured logging, automated testing, and cloud deployment.

## 🚀 Live Demo

**Base URL**

https://cloud-health-api.onrender.com

## 📡 Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Application information |
| `/health` | Health status, timestamp, startup time, and uptime |
| `/ready` | Readiness check |
| `/metrics` | Python runtime and platform information |
| `/version` | API version information |

## 🛠️ Technologies

- Python 3.13
- Flask
- Pytest
- Docker
- Git & GitHub
- Render

## ✅ Features

- RESTful API
- JSON responses
- Health monitoring
- Readiness endpoint
- Metrics endpoint
- Version endpoint
- Structured logging
- Custom JSON 404 responses
- Global exception handling
- Automated tests with Pytest
- Cloud deployment on Render

## 🧪 Running Tests

```bash
python -m pytest
```

## 🌐 Deployment

This application is deployed on Render and publicly accessible at:

https://cloud-health-api.onrender.com

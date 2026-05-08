# Flask Blog DevOps 🚀

![CI Pipeline](https://github.com/DarkMuster/flask-blog-devops/actions/workflows/ci.yml/badge.svg)
![CD Staging](https://github.com/DarkMuster/flask-blog-devops/actions/workflows/cd-staging.yml/badge.svg)

A full DevOps pipeline built around a Flask Blog application.

## 📋 Table of Contents
- [About](#about)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Monitoring](#monitoring)

## About
Flask Blog is a web application that allows users to create, publish and manage blog posts with user authentication and comments. This project focuses on industrializing the application lifecycle with a complete DevOps pipeline.

## Tech Stack
| Domain | Technology |
|---|---|
| Application | Python 3.11 / Flask |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Testing | pytest + coverage.py |
| CI/CD | GitHub Actions |
| Containerization | Docker + Docker Compose |
| Deployment | Railway |
| Monitoring | Prometheus + Grafana |
| Code Quality | flake8, black, isort, bandit |

## Getting Started

### Prerequisites
- Python 3.11+
- Git
- Docker (optional)

### Local Setup
```bash
# Clone the repo
git clone https://github.com/DarkMuster/flask-blog-devops.git
cd flask-blog-devops

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run the app
python run.py
```

Open http://localhost:5000 in your browser.

## Running Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=flaskblog --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_models.py -v
```

## Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Services:
# App      → http://localhost:5000
# Nginx    → http://localhost:80
# Grafana  → http://localhost:3000
# Prometheus → http://localhost:9090
```

## CI/CD Pipeline
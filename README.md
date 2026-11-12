# Containerized Application Deployment and Management Using Docker

## About the Project

This is a BCA Cloud Computing project developed by Team 14.

The project demonstrates how to build and deploy a Flask web application using Docker containers. It also uses PostgreSQL as the database and AWS EC2 for cloud deployment.

## Technologies Used

- Python
- Flask
- HTML and CSS
- Docker
- Docker Compose
- PostgreSQL
- AWS EC2

## Project Features

- Flask-based web application.
- Docker containerization.
- PostgreSQL database connectivity.
- Application status dashboard.
- Deployment on AWS EC2.
- Automatic container restart after system reboot.

## Project Structure

```text
Docker_Project/
│
├── templates/
│   └── index.html
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── .gitignore
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/amritharajesh321/Docker_Project-BCA.git
```

2. Open the project folder:

```bash
cd Docker_Project-BCA
```

3. Create a `.env` file and configure the PostgreSQL database connection details.

4. Build and start the Docker container:

```bash
docker compose up -d --build
```

5. Open the application in your browser:

```text
http://localhost:5000
```

## Cloud Deployment

The application is deployed on an AWS EC2 Ubuntu instance using Docker and Docker Compose.

## Team Details

**Team Number:** 14  
**Project:** BCA Cloud Computing  
**Year:** 2026
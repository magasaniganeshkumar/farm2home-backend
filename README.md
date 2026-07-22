# 🌱 Farm2Home Backend

A production-ready Django REST Framework backend for the Farm2Home platform.

## 📌 Project Overview

Farm2Home is an agricultural e-commerce platform that connects farmers directly with customers.

The backend is being built using enterprise software engineering practices with Django, Django REST Framework, Docker, and AWS.

---

## 🚀 Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- SQLite (Development)
- Amazon RDS MySQL (Production)

### Authentication
- Custom User Model
- JWT Authentication (Upcoming)

### API Documentation
- Swagger (drf-spectacular)

### Cloud (Upcoming)
- AWS ECS
- Amazon RDS
- Amazon S3
- Amazon ECR
- CloudWatch

### DevOps (Upcoming)
- Docker
- Docker Compose
- GitHub Actions
- AWS CodeBuild
- AWS CodePipeline

---

## 📂 Project Structure

```text
farm2home-backend/
│
├── apps/
│   ├── accounts/
│   ├── core/
│
├── config/
├── docs/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

## ✅ Completed Features

- Project setup
- Environment-based settings
- Custom User Model
- UUID Primary Keys
- BaseModel
- Soft Delete
- User Registration API
- Swagger Documentation

---

## 🚧 Upcoming Features

- JWT Authentication
- Products Module
- Categories
- Cart
- Orders
- Payments
- Notifications
- Email Verification
- Docker Deployment
- AWS Deployment
- CI/CD Pipeline
- Analytics Integration

---

## 🛠️ Local Setup

Clone the repository:

```bash
git clone <repository-url>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

---

## 📖 API Documentation

Swagger:

```
/api/docs/
```

OpenAPI Schema:

```
/api/schema/
```

---

## 👨‍💻 Author

Ganesh Reddy

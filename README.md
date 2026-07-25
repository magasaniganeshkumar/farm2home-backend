# 🌱 Farm2Home Backend

A production-ready Django REST Framework backend powering the Farm2Home platform.

---

# 📌 Project Overview

Farm2Home is an agricultural e-commerce and supply chain platform that connects farmers directly with customers while enabling Farm2Home to manage procurement, warehouses, inventory, and deliveries.

The backend is being built using enterprise software engineering practices with Django, Django REST Framework, Docker, and AWS Cloud.

---

# 🚀 Tech Stack

## Backend

- Python 3.14
- Django 6
- Django REST Framework

## Database

- SQLite (Development)
- Amazon RDS MySQL (Production)

## Authentication

- Custom User Model
- JWT Authentication
- Refresh Token Rotation
- Token Blacklisting
- Password Reset
- Change Password

## API Documentation

- Swagger UI (drf-spectacular)
- OpenAPI Schema

## Cloud (Upcoming)

- AWS ECS
- Amazon RDS
- Amazon S3
- Amazon ECR
- CloudWatch

## DevOps (Upcoming)

- Docker
- Docker Compose
- GitHub Actions
- AWS CodeBuild
- AWS CodePipeline

---

# 📂 Project Structure

```text
farm2home-backend/
│
├── apps/
│   ├── accounts/
│   ├── core/
│   ├── locations/
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

# ✅ Completed Modules

## Core

- Environment-based Settings
- BaseModel
- UUID Primary Keys
- Soft Delete
- Custom Managers

---

## Authentication

- Custom User Model
- User Registration
- JWT Login
- User Profile
- Logout
- Change Password
- Forgot Password
- Reset Password
- Refresh Token
- Token Blacklisting

---

## Location Management

- Customer Address Management
- Create Address
- List Addresses
- Retrieve Address
- Update Address
- Soft Delete Address
- Default Address Support
- JWT Protected APIs

---

# 🚧 Upcoming Modules

## Sprint 3

- Farmer Management
- Farm Management

## Sprint 4

- Crop Management
- Dairy Management
- Livestock Management

## Sprint 5

- Procurement
- Warehouse Management
- Inventory Management

## Sprint 6

- Product Catalog
- Categories
- Product Images

## Sprint 7

- Shopping Cart
- Wishlist
- Customer Orders

## Sprint 8

- Payments
- Delivery Management
- Notifications

## Sprint 9

- Analytics
- Reports
- Admin Dashboard

---

# 🔐 Authentication APIs

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/accounts/register/` |
| POST | `/api/v1/accounts/login/` |
| POST | `/api/v1/accounts/logout/` |
| POST | `/api/v1/accounts/token/refresh/` |
| GET | `/api/v1/accounts/me/` |
| POST | `/api/v1/accounts/change-password/` |
| POST | `/api/v1/accounts/forgot-password/` |
| POST | `/api/v1/accounts/reset-password/` |

---

# 📍 Location APIs

| Method | Endpoint |
|---------|----------|
| GET | `/api/v1/locations/` |
| POST | `/api/v1/locations/` |
| GET | `/api/v1/locations/{id}/` |
| PATCH | `/api/v1/locations/{id}/` |
| DELETE | `/api/v1/locations/{id}/` |

---

# 🛠️ Local Development

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run development server

```bash
python manage.py runserver
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema

```
http://127.0.0.1:8000/api/schema/
```

---

# 📌 Current Project Status

| Module | Status |
|---------|--------|
| Core | ✅ Completed |
| Authentication | ✅ Completed |
| Location | ✅ Completed |
| Farmer | 🚧 In Progress |
| Farm | ⏳ Planned |
| Products | ⏳ Planned |
| Warehouse | ⏳ Planned |
| Orders | ⏳ Planned |
| Payments | ⏳ Planned |

---

# 👨‍💻 Author

**Ganesh Reddy**

Backend Developer | Python | Django | AWS | Data Engineering

---

# 📄 License

This project is being developed as the backend for the Farm2Home platform.
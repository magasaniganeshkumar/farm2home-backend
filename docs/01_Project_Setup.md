# Project Setup

## Project Name

Farm2Home Backend

---

## Description

Farm2Home is an agricultural e-commerce platform that connects farmers with customers.

The backend is developed using Django REST Framework following enterprise architecture and best practices.

---

## Technology Stack

### Backend

- Python 3.14
- Django 6
- Django REST Framework

### Database

- SQLite (Development)
- Amazon RDS MySQL (Production)

### API Documentation

- drf-spectacular
- Swagger UI

### Authentication

- JWT
- Refresh Tokens
- Token Blacklisting

---

## Project Structure

apps/
- core
- accounts
- locations

config/

docs/

tests/

---

## Local Setup

Create virtual environment

```bash
python -m venv venv
```

Activate

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

Run server

```bash
python manage.py runserver
```
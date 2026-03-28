# ClinicLink

A production-ready, real-time clinic appointment and queue management system designed for the Pakistani market, initially targeting Gujranwala. Features real-time token tracking via WebSockets, Twilio SMS integration, and a dedicated clinic dashboard.

## Overview
Built with **Django 5**, **Django Channels**, **Celery**, **Tailwind CSS**, and **Alpine.js**.

## Core Features
- **Real-time Queue Tracking:** Patients track their token position live via WebSockets.
- **Universal Booking Modal:** Patients book easily via Alpine.js components communicating with JSON APIs.
- **Automated SMS via Twilio:** Confirmation, Delay Alerts, and "You are next" notices via Celery.
- **Staff Dashboard:** Clinic operators can bump queues, mark no-shows, and trigger delay alerts to the whole queue instantly.

## Setup Instructions

### 1. Requirements
- Python 3.10+
- Redis (Required for Channels and Celery)
- PostgreSQL (Production) / SQLite (Development)

### 2. Environment Configuration
Create a `.env` file from the `.env.example` file.
```bash
cp .env.example .env
```
Ensure you have Redis running: `redis-server`

### 3. Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Database Setup
Now that the `accounts` app and custom user model are defined, run migrations:
```bash
python manage.py makemigrations accounts clinics appointments notifications dashboard
python manage.py migrate
```

### 5. Running the Application
You will need to run three separate processes:

**Process 1: Django Server (ASGI for WebSockets)**
```bash
daphne -p 8000 cliniclink.asgi:application
# or for standard development parsing both HTTP and WS natively:
python manage.py runserver
```

**Process 2: Celery Worker (SMS & Async Tasks)**
```bash
celery -A cliniclink worker -l info
```

**Process 3: Redis Server**
*(Ensure your Redis instance is active on port 6379).*

## Development Guidelines
- Always use the predefined Tailwind classes mirroring the exact Figma/HTML prototype supplied in `Prompt 1`.
- WebSockets use `ws/queue/patient/<token>` and `ws/queue/dashboard/<clinic_id>`.
- Keep business logic inside `services.py` layers.

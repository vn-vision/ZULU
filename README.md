# ZULU RE

## Overview

*ZULU* is a real estate web application featuring a Django backend and a React frontend.

## Project Structure

```plaintext
ZULU/
├── backend/                 # Django backend directory
│   ├── manage.py
│   ├── backend/             # Main Django project folder
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   ├── api/                 # Django app for APIs
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py
│   ├── venv/                # Virtual environment for Django
│   ├── requirements.txt     # List of Python packages required
├── frontend/                # React frontend directory
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
├── .gitignore
├── README.md
```
## Installation, backend:
```bash
 - cd backend
 - python3 -m venv venv
 - pip install -r requirements.txt
 - python manage.py migrate # apply migrations and create database
 - python manage.py createsuperuser # create admin user
 - python manage.py runserver # start the backend server
```

## Installation, frontend:
```bash
 - cd frontend
 - npm start
```

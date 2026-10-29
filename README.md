# Django DevOps Lab

A simple Django Hello World application created as part
of a multi-stack AWS deployment learning project.

## Requirements
- Python
- pip
- Django

## Local setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver 127.0.0.1:8001

## Test

Open http://127.0.0.1:8001/

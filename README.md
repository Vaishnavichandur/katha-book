# Sri Lakshmi Gold & Jewellers CRM (Django API)

Quick start:

1) Create venv and install deps
   python -m venv .venv && . .venv/bin/activate
   pip install -r requirements.txt

2) Migrate and create superuser
   python manage.py migrate
   python manage.py createsuperuser

3) Run server
   export FRONTEND_ORIGIN=http://localhost:3000
   python manage.py runserver 0.0.0.0:8000

Default API root: http://localhost:8000/api/
JWT endpoints: /api/token/ and /api/token/refresh/

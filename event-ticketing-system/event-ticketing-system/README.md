# Event Ticketing System

Skeleton project created by script.

This repository contains the basic structure for a Django-based event ticketing system.

Files and folders:
- `ticketing_system/` - main Django project package
- `apps/` - Django apps: accounts, core, vendors
- `templates/` - HTML templates

How to use:
- Create a Python virtual environment
- Install packages from `requirements.txt`
- Run `python manage.py runserver` after configuring settings

Running locally (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
# Create a superuser interactively:
python manage.py createsuperuser
# Or create from environment variables:
$env:SUPERADMIN_USERNAME='admin'; $env:SUPERADMIN_EMAIL='admin@example.com'; $env:SUPERADMIN_PASSWORD='secret'; python manage.py create_superadmin
python manage.py runserver
```

Notes:
- A sample `static/css/style.css` is included. If you prefer a different static layout, edit `ticketing_system/settings.py`.
- The `create_superadmin` command will create a superuser from `SUPERADMIN_*` env vars or fall back to `createsuperuser`.

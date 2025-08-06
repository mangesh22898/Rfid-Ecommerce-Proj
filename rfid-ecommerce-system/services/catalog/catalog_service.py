# catalog_service.py
import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

# Run Django development server
execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])

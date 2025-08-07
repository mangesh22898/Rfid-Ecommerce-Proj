import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

execute_from_command_line(["email_service", "runserver", "0.0.0.0:8000"])

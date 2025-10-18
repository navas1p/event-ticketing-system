import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Create a superadmin user from environment variables or fall back to interactive createsuperuser.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('SUPERADMIN_USERNAME')
        email = os.environ.get('SUPERADMIN_EMAIL')
        password = os.environ.get('SUPERADMIN_PASSWORD')

        if username and password:
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING(f"Superadmin '{username}' already exists."))
                return
            User.objects.create_superuser(username=username, email=email or '', password=password)
            self.stdout.write(self.style.SUCCESS(f"Created superadmin '{username}'."))
            return

        self.stdout.write('SUPERADMIN_* env vars not found. Falling back to interactive createsuperuser.')
        call_command('createsuperuser')

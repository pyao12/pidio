import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pidio.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

django.setup()

from django.contrib.auth import get_user_model

def main():
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="test@example.com",
            password="123456"
        )
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")

if __name__ == "__main__":
    main()
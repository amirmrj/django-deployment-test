import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projecttwo.settings')
import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def add_user(N=5):
    for e in range(N):
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.free_email()

        user = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname, email=fake_email)[0]

if __name__ == '__main__':
    print("populating")
    add_user(20)
    print("population completed")

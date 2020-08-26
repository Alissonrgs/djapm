# python
from random import randint

# django
from django.contrib.auth.models import User
from django.db import IntegrityError

# third party
import names


def run():
    for _ in range(0, 100):
        gender = 'male' if randint(0, 1) else 'female'
        is_active = True if randint(0, 1) else False
        is_superuser = True if randint(0, 1) else False

        first_name, last_name = names.get_full_name(gender=gender).split()
        username = first_name.lower()
        password = username

        try:
            user, create = User.objects.create(
                username=username, first_name=first_name, last_name=last_name,
                is_staff=is_superuser, is_superuser=is_superuser, is_active=is_active)
            if create:
                user.set_password(password)
                user.save()
        except IntegrityError as err:
            print(err)
            continue

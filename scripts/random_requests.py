# python
import time

from math import ceil
from random import randint
from random import choice

# django
from django.contrib.auth.models import User
from django.test import Client

# third party
from rest_framework.settings import api_settings


def run():
    users = User.objects.only('first_name', 'last_name', 'username').order_by('?')
    users_count = users.count()

    while True:
        for _ in range(0, randint(0, 100)):
            user = choice(users)

            client = Client()
            login_status = client.login(username=user.username, password=user.username)

            page = randint(1, ceil(users_count / api_settings.PAGE_SIZE))
            url = f'/api/users/?page={page}'
            response = client.get(url)
            client.logout()

            print(f'{user.username}: {user.get_full_name()} - '
                  f'login: {login_status} - request: {url} - {response.status_code}')
        time.sleep(10)

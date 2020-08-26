# python
import time

from random import randint
from random import choice

# django
from django.contrib.auth.models import User

# project
from accounts.tasks import user_count_task
from accounts.tasks import user_full_name_task


def run():
    users = User.objects.only('first_name', 'last_name', 'username').order_by('?')

    while True:
        for _ in range(0, randint(0, 100)):
            user = choice(users)

            random_task = user_count_task if randint(0, 1) else user_full_name_task
            if random_task == user_count_task:
                random_task.apply_async()
            else:
                random_task.apply_async(args=[user.id])

            print(f'{user.username}: {user.get_full_name()} - task: {random_task.__name__}')
        time.sleep(10)

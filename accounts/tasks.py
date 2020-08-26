from __future__ import absolute_import

# django
from django.contrib.auth.models import User

# third party
from celery import shared_task


@shared_task
def user_full_name_task(user_id):
    user = User.objects.get(id=user_id)
    return user.get_full_name()


@shared_task
def user_count_task():
    return User.objects.filter(is_active=True).count()

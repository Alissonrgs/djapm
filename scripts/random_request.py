import requests
import time

from random import randint


def run():
    while True:
        times = randint(1, 100)

        for _ in range(0, times):
            requests.get('http://localhost:8000/api/users/?format=json')

        time.sleep(2)

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anime_project.settings")
django.setup()

from anime.utils import fetch
from time import sleep

for id in range(1, 1000):
    fetch(id)
    sleep(0.5)

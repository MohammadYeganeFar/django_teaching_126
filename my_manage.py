import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maktab_django_126.settings')
setup()
from first_app.models import *

a = BlogPost.objects.filter(authors__first_='mmd') 
print(a)
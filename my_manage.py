import os
from django import setup
from django.db import connection
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maktab_django_126.settings')
setup()
from first_app.models import *

with open('/home/mohammad-yegane-far/Downloads/first_app_blogpost (5).sql', 'r') as f:
    data = f.read()

stmts = [s.strip() for s in data.split(';') if s.strip()]

# with connection.cursor() as cursor:
#     for stmt in stmts:
#         cursor.execute(stmt)
        # break
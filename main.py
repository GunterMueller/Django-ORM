############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
import csv
from django.http import HttpResponse

sys.dont_write_bytecode = True

filePath = '/home/gunter/GM_Programming/PLAY_GROUNDS/Python/sqlite3_orm/'
fileName = 'orm_export.csv'

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
from djqscsv import write_csv

django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

model_class = User

meta = model_class._meta
field_names = [field.name for field in meta.fields]

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')


qs = User.objects.all()
with open(filePath + fileName, 'wb') as csv_file:
  write_csv(qs, csv_file)


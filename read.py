import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GuessIt.settings')
import django
django.setup()

from what_am_i.models import Words
# Read CSV file and insert into database
with open("data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Words.objects.create(word=row["word"], joke=row["joke"])
print("done")

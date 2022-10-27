import codecs
import os
import sys

project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'
import django

django.setup()
from django.db import DatabaseError

from scraping.models import City, Language, Vacancy, Error

from scraping.parsers import *

parsers = ((work, 'https://www.work.ua/jobs-dnipro-python/'),
           (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%94%D0%BD%D1%96%D0%BF%D1%80%D0%BE&category=Python'),
           (djinni, 'https://djinni.co/jobs/?primary_keyword=Python&region=UKR&location=dnipro')
           )
city = City.objects.filter(slug='dnipro').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
    if errors:
        er = Error(data=errors).save()

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()

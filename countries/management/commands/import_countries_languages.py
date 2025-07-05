# countries/management/commands/import_countries_languages.py
import json
from django.core.management.base import BaseCommand
from countries.models import Country, Language

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('countries.json', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            if 'country' not in item or 'languages' not in item:
                print('Error:', item)
                continue
            country, _ = Country.objects.get_or_create(name=item['country'])
            for lang in item['languages']:
                language, _ = Language.objects.get_or_create(name=lang)
                country.languages.add(language)
        self.stdout.write(self.style.SUCCESS('Successfully imported languages'))
import json

from django.core.management import BaseCommand

from countries.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('countries.json') as f:
            data = json.load(f)
        for item in data:
            Country.objects.get_or_create(name=item['country'])
        self.stdout.write(self.style.SUCCESS('Successfully imported countries'))
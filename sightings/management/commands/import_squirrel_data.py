from django.core.management.base import BaseCommand
from django.utils import timezone
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Data import'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        sightings = []
        for dict_ in data:
            sightings.append(Squirrel(
                latitude=float(dict_['Y']),
                longitude=float(dict_['X']),
                unique_squirrel_id=dict_['Unique Squirrel ID'],
                shift=dict_['Shift'].lower(),
                date=timezone.datetime.strptime(dict_['Date'], '%m%d%Y').date(),
                age=dict_['Age'],
                primary_fur_color=dict_['Primary Fur Color'],
                specific_location=dict_['Specific Location'],
                running=dict_['Running'].lower() == 'true',
                chasing=dict_['Chasing'].lower() == 'true',
                climbing=dict_['Climbing'].lower() == 'true',
                eating=dict_['Eating'].lower() == 'true',
                foraging=dict_['Foraging'].lower() == 'true',
                other_activities=dict_['Other Activities'],
                kuks=dict_['Kuks'].lower() == 'true',
                quaas=dict_['Quaas'].lower() == 'true',
                moans=dict_['Moans'].lower() == 'true',
                tail_flags=dict_['Tail flags'].lower() == 'true',
                tail_twitches=dict_['Tail twitches'].lower() == 'true',
                approaches=dict_['Approaches'].lower() == 'true',
                indifferent=dict_['Indifferent'].lower() == 'true',
                runs_from=dict_['Runs from'].lower() == 'true',
            ))

        Sighting.objects.bulk_create(sightings)

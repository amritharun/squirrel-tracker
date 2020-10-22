
from django.core.management.base import BaseCommand

import csv

from tracker.models import Sighting

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        dict_ = {} 
        s = Sighting.objects.all()
        with open(options['csv_file'],"w") as fp:
            for i in s:
                dict_['Longitude'] = i.LONG
                dict_['Latitude'] = i.LAT
                dict_['Shift'] = i.SHIFT
                dict_['Date'] = i.DATE
                dict_['Unique Squirrel ID'] = i.S_ID
                dict_['Age'] = i.AGE
                dict_['Primary Fur Color'] = i.COLOR
                dict_['Location'] = i.LOCATION
                dict_['Specific Location'] = i.SPEC_LOCATION
                dict_['Running'] = i.RUNNING
                dict_['Chasing'] = i.CHASING
                dict_['Climbing'] = i.CLIMBING
                dict_['Eating'] = i.EATING
                dict_['Foraging'] = i.FORAGING
                dict_['Other Activities'] = i.OTHER
                dict_['Kuks'] = i.KUK
                dict_['Quaas'] = i.QUAAS
                dict_['Moans'] = i.MOAN
                dict_['Tail Flags'] = i.TAIL_FLAG
                dict_['Tail Twitches'] = i.TAIL_TWITCH
                dict_['Approaches'] = i.APPROACH
                dict_['Runs from'] = i.RUNS
                writer = csv.DictWriter(fp,delimiter=",",fieldnames=dict_.keys())
                writer.writeheader()
                writer.writerow(dict_)



import csv
from datetime import datetime

from django.core.management import BaseCommand
from tracker.models import Sighting 
import argparse

from distutils.util import strtobool

class Command(BaseCommand):
        help = ('Load squirrel data from csv into DB')
            
        def add_arguments(self,parser):
            parser.add_argument('path', type=str)

        def handle(self, *args, **kwargs):
            Sighting.objects.all().delete()
            path = kwargs['path']
            counter = 0
            with open(path, 'rt') as f:
                unique = set()
                reader = csv.reader(f, dialect='excel')
                next(reader,None)
                for row in reader:
                    counter += 1
                    # print(counter)
                    if row[2] in unique:
                        continue
                    unique.add(row[2])
                    sighting = Sighting.objects.create(
                            LONG=row[0],
                            LAT=row[1],
                            S_ID=row[2],
                            SHIFT=row[4],
                            DATE=datetime.strptime(row[5], '%m%d%Y'),
                            AGE=row[7],
                            COLOR=row[8],
                            LOCATION=row[12],
                            SPEC_LOCATION=row[14],
                            RUNNING=(row[15]=='true'),
                            CHASING=(row[16]=='true'),
                            CLIMBING=(row[17]=='true'),
                            EATING=(row[18]=='true'),
                            FORAGING=(row[19]=='true'),
                            OTHER=row[20],
                            KUK=(row[21]=='true'),
                            QUAAS=(row[22]=='true'),
                            MOAN=(row[23]=='true'),
                            TAIL_FLAG=(row[24]=='true'),
                            TAIL_TWITCH=(row[25]=='true'),
                            APPROACH=(row[26]=='true'),
                            RUNS=(row[27]=='true'),
                            )
                    sighting.save()
                     


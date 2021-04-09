import csv
from django.core.management.base import BaseCommand
from dateutil import parser
import re
from sightings.models import Squirrel
from datetime import date


class Command(BaseCommand):
    help = 'Import squirrel data file to the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path, 'rt') as f:
            excel_reader = csv.reader(f, dialect='excel')
            next(excel_reader)
            squirrel_tracker = list()
            for row in excel_reader:
                if row[2] in squirrel_tracker:
                    continue
                else:
                    month, day, year = pattern.match(row[5]).groups()
                    squirrel = Squirrel.objects.get_or_create(
                        X=row['X'],
                        Y=row['Y'],
                        Unique_squirrel_id=row['Unique Squirrel ID'],
                        Shift=row['Shift'],
                        Date=date(int(year), int(month), int(day)),
                        Age=row['Age'],
                        Primary_Fur_Color=row['Primary Fur Color'],
                        Location=row['Location'],
                        Specific_location=row['Specific Location'],
                        Running=True if row['Running'] == 'TRUE' else False,
                        Chasing=True if row['Chasing'] == 'TRUE' else False,
                        Climbing=True if row['Climbing'] == 'TRUE' else False,
                        Eating=True if row['Eating'] == 'TRUE' else False,
                        Foraging=True if row['Foraging'] == 'TRUE' else False,
                        Other_Activities=True if row['Other Activities'] == 'TRUE' else False,
                        Kuks=True if row['Kuks'] == 'TRUE' else False,
                        Quaas=True if row['Quaas'] == 'TRUE' else False,
                        Moans=True if row['Moans'] == 'TRUE' else False,
                        Tail_Flags=True if row['Tail flags'] == 'TRUE' else False,
                        Tail_Twitches=True if row['Tail twitches'] == 'TRUE' else False,
                        Approaches=True if row['Approaches'] == 'TRUE' else False,
                        Indifferent=True if row['Indifferent'] == 'TRUE' else False,
                        Runs_From=True if row['Runs from'] == 'TRUE' else False
                    )
                    squirrel_tracker.append(row[2])

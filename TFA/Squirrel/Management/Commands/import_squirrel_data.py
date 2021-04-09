import csv
from django.core.management.base import BaseCommand
from dateutil import parser
from sightings.models import Squirrel
from datetime import date

class Command(BaseCommand):
    help = 'Import squirrel data file to the database'

    def add_arguments(self,parser):
        parser.add_argument('path', type =str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        try:
            with open(path, encoding='utf-8') as f:
                excel_reader = csv.DictReader(f)
                for row in excel_reader:
                    s = Squirrels(
                        X=row['X'],
                        Y=row['Y'],
                        Unique_squirrel_id=row['Unique Squirrel ID'],
                        Shift=row['Shift'],
                        Date=datetime.date(
                            int(row['Date'][-4:]), int(row['Date'][:2]), int(row['Date'][2:4])),
                        Age=row['Age'],
                        Primary_Fur_Color=row['Primary Fur Color'],
                        Location=row['Location'],
                        Specific_location=row['Specific Location'],
                        Running=row['Running'].upper(),
                        Chasing=row['Chasing'].upper(),
                        Climbing=row['Climbing'].upper(),
                        Eating=row['Eating'].upper(),
                        Foraging=row['Foraging'].upper(),
                        Other_activities=row['Other Activities'],
                        Kuks=row['Kuks'].upper(),
                        Quaas=row['Quaas'].upper(),
                        Moans=row['Moans'].upper(),
                        Tail_flags=row['Tail flags'].upper(),
                        Tail_twitches=row['Tail twitches'].upper(),
                        Approaches=row['Approaches'].upper(),
                        Indifferent=row['Indifferent'].upper(),
                        Runs_from=row['Runs from'].upper(),
                    )
                    s.save()
        except csv.Error as e:
            print(f'there is something wrong with {excel_reader.line_num}')





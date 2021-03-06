# Generated by Django 3.1.7 on 2021-04-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(help_text='Longitude')),
                ('Y', models.FloatField(help_text='Latitude')),
                ('Unique_Squirrel_ID', models.CharField(max_length=100, null=True, unique=True)),
                ('Hectare', models.CharField(max_length=100)),
                ('Shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=100)),
                ('Date', models.DateField(blank=True)),
                ('Hectare_Squirrel_Number', models.CharField(max_length=100)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=100, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray')], max_length=20, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=100, null=True)),
                ('Specific_Location', models.CharField(blank=True, max_length=100)),
                ('Running', models.BooleanField(blank=True)),
                ('Chasing', models.BooleanField(blank=True)),
                ('Climbing', models.BooleanField(blank=True)),
                ('Eating', models.BooleanField(blank=True)),
                ('Foraging', models.BooleanField(blank=True)),
                ('Other_activities', models.CharField(blank=True, max_length=100)),
                ('Kuks', models.BooleanField(blank=True)),
                ('Quaas', models.BooleanField(blank=True)),
                ('Moans', models.BooleanField(blank=True)),
                ('Tail_flags', models.BooleanField(blank=True)),
                ('Tail_twitches', models.BooleanField(blank=True)),
                ('Approaches', models.BooleanField(blank=True)),
                ('Indifferent', models.BooleanField(blank=True)),
                ('Runs_from', models.BooleanField(blank=True)),
            ],
        ),
    ]

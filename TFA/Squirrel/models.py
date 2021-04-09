from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


class Meta:
    managed = True


class Squirrel(models.Model):
    X = models.FloatField(
        help_text=_('Longitude'),
        blank=False
    )

    Y = models.FloatField(
        help_text=_('Latitude'),
        blank=False
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=False
    )

    Hectare = models.CharField(
        max_length=100
    )

    Shift = models.CharField(
        max_length=2,
        blank=True,
    )

    Date = models.DateField(
        blank=True
    )

    Hectare_Squirrel_Number = models.CharField(
        max_length=100
    )

    Age = models.CharField(
        max_length=100,
        blank=True,
    )

    Primary_Fur_Color = models.CharField(
        max_length=100,
        blank=True,
    )

    Location = models.CharField(
        max_length=100,
        blank=True
    )

    Specific_Location = models.CharField(
        max_length=100,
        blank=True
    )

    Running = models.BooleanField(
        blank=True
    )

    Chasing = models.BooleanField(
        blank=True
    )

    Climbing = models.BooleanField(
        blank=True
    )

    Eating = models.BooleanField(
        blank=True
    )

    Foraging = models.BooleanField(
        blank=True
    )

    Other_activities = models.CharField(
        max_length=100,
        blank=True)

    Kuks = models.BooleanField(
        blank=True
    )

    Quaas = models.BooleanField(
        blank=True)

    Moans = models.BooleanField(
        blank=True
    )

    Tail_flags = models.BooleanField(
        blank=True)

    Tail_twitches = models.BooleanField(
        blank=True)

    Approaches = models.BooleanField(
        blank=True
    )

    Indifferent = models.BooleanField(
        blank=True
    )
    Runs_from = models.BooleanField(
        blank=True
    )

    def __str__(self):
        return self.Unique_Squirrel_ID  # Change to Unique_squirrel_id

    def return_url(self):
        return reverse('Squirrel-Detail', kwargs={'-id': self.Unique_Squirrel_ID})  # Change to Unique_squirrel_id

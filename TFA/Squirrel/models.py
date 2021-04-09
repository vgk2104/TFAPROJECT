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

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM')
    )

    Shift = models.CharField(
        max_length=100,
        choices=SHIFT_CHOICES,
        blank=True,
    )

    Date = models.DateField(
        blank=True
    )

    Hectare_Squirrel_Number = models.CharField(
        max_length=100
    )

    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = (
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
    )

    Age = models.CharField(
        max_length=100,
        choices=AGE_CHOICES,
        blank=True,
        null=True, )

    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    GRAY = 'Gray'

    COLOR_CHOICES = (
        (BLACK, 'Black'),
        (CINNAMON, 'Cinnamon'),
        (GRAY, 'Gray'),
    )

    Primary_Fur_Color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        null=True,
        blank=True,
    )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'

    LOCATION_CHOICES = (
        (Ground_Plane, 'Ground Plane'),
        (Above_Ground, 'Above Ground'),
    )

    Location = models.CharField(
        max_length=100,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
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

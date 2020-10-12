from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.forms import ModelForm

#Create Squirrel model
class Squirrel(models.Model):

    X = models.FloatField(
        help_text=_('X'),
        null=True,
    )
    
    Y = models.FloatField(
        help_text=_('Y'),
        null=True,
    )
Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=14,
        primary_key=True,
    )

    Hectare = models.CharField(
        help_text=_('Hectare'),
        max_length = 3,
        null=True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID

    AM = 'AM'
    PM = 'PM'

    Shift = models.CharField(
        help_text=_('Shift'),
        choices = (
            (AM, 'AM'),
            (PM, 'PM'),
        ),
        default = AM,
        max_length =2,
        null=True,
    )

    Date = models.DateField(
        help_text=_('Date'),
        null=True,
    )

    Hectare_Squirrel_Number = models.CharField(
        help_text=_('Hectare Squirrel Number'),
        max_length=10,
        null=True,
    )
    


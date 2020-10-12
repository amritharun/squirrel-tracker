from django.db import models
from django.utils.translation import gettext as _

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
    


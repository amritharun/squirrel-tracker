from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator

class Sighting(models.Model):
    LONG = models.DecimalField(
            help_text=_('Longitude'),
            blank = True,
            max_digits=50,
            decimal_places = 20,
            )
    LAT = models.DecimalField(
            help_text=_('Latitude'),
            blank = True,
            max_digits=50,
            decimal_places = 20,
            )
    S_ID= models.CharField(
         max_length=100,
         validators=[MinLengthValidator(10)],
         help_text=_('Unique Sighting ID'),
         primary_key= True,
         default='1234',
         unique=True
         )

    AM='AM'
    PM='PM'
    shift = ((AM,'AM'),(PM,'PM'))
    SHIFT = models.CharField(
            max_length = 100,
            choices = shift,
            help_text = _('Shift session'),
            blank = True
            )
    DATE = models.DateField(
            help_text = _('Date of sighting')
            )
    ADULT='Adult'
    JUVENILE = 'Juvenile'
    age = ((ADULT,'Adult'), (JUVENILE,'Juvenile'))

    AGE = models.CharField(
            max_length=100,
            choices = age, 
            help_text=_('adult or juvenile'),
            blank = True,
            )
    GREY= 'Grey'
    CINNAMON= 'Cinnamon'
    BLACK = 'Black'
    color = ((GREY,'Grey'),(CINNAMON, 'Cinnamon'),(BLACK,'Black'))
    COLOR = models.CharField(
            max_length=100,
            blank=True,
            choices= color,
            help_text=_('squirrel color'),
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    location = ((GROUND_PLANE,'Ground Plane'), (ABOVE_GROUND, 'Above Ground'))
    LOCATION = models.CharField(
            max_length=100,
            choices = location,
            help_text=_('squirrel found location'),
            blank = True,
            )
    SPEC_LOCATION = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('Any additional comments about location'),
         )
    RUNNING = models.BooleanField(
            help_text=_('Running!'),
            default = False,
            )
    CHASING = models.BooleanField(
            help_text=_('Chasing!'),
            default = False,
            )
    CLIMBING= models.BooleanField(
            help_text=_('Climbing!'),
            default = False,
            )
    EATING= models.BooleanField(
            help_text=_('Eating'),
            default = False,
            )
    FORAGING= models.BooleanField(
            help_text=_('Foraging'),
            default = False,
            )
    OTHER= models.CharField(
            max_length=500,
            blank=True,
            help_text=_('any additional comments')
           )
    KUK= models.BooleanField(
            help_text=_('Kuking'),
            default = False,
            )
    QUAAS= models.BooleanField(
            help_text=_('Quaaing'),
            default = False,
            )
    MOAN= models.BooleanField(
            help_text=_('Moaning'),
            default = False,
            )
    TAIL_FLAG = models.BooleanField(
            help_text=_('Flagging tail'),
            default = False,
            )
    TAIL_TWITCH= models.BooleanField(
            help_text=_('Twitching tail'),
            default = False,
            )
    APPROACH = models.BooleanField(
            help_text=_('Approached humans'),
            default = False,
            )
    RUNS= models.BooleanField(
            help_text=_('Runs from humans'),
            default = False,
            )





# Create your models here.

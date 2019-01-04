from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from djproject.settings import *

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Well_Profile(models.Model):
    #well_id = models.AutoField(primary_key=True, blank = True, null = True)
    well_name = models.CharField(max_length=50, blank = True, default='')
    API10 = models.IntegerRangeField(min_length=10, max_length=10)
    engineer = models.ManyToManyField(User)

    company_choices = (
    ('Oxy', 'Oxy'),
    ('Tri-C', 'Tri-C'),
    ('Riverbend', 'Riverbend'),
    )

    company = models.CharField(max_length=100, choices=company_choices, default='')

    team_choices = (
    ('Asset team 1', 'Asset team 1'),
    ('Asset team 2', 'Asset team 2'),
    ('Asset team 3', 'Asset team 3'),
    )
    team = models.CharField(max_length=100, choices=team_choices, default='')
    asset_choices = (
    ('TX Asset 1', 'TX Asset 1'),
    ('TX Asset 2', 'TX Asset 2'),
    ('NM Asset 1', 'NM Asset 1'),
    ('NM Asset 2', 'NM Aseet 2'),
    )
    asset = models.CharField(max_length=100, choices=asset_choices, default='')
    region_choices = (
    ('TX Delaware Basin', 'Tx Delaware Basin'),
    ('Midland Basin', 'Midland Basin'),
    ('NM Delaware Basin', 'NM Delaware Basin')
    )
    region = models.CharField(max_length=100, choices=region_choices, default='')

    #welltype_choices = (
    #('WCA10k', 'WCA_10k'),
    #('WCA7.5k', 'WCA_7500'),
    #('1BS10k', '1BS_10k'),
    #('WCB10k', 'WCB_10k'),
    #('WCC10k', 'WCC_10k'),
    #('2BS10k', '2BS_10k'),
    #('3BS10k', '3BS_10k'),
    #('HOBAN10k', 'Hoban_10k'),
    #('HOBAN5k', 'Hoban_5k'),
    #)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(null = True)
    def save(self, *args, **kwargs):
        #''' On save, update timestamps '''
        if not self.well_name:
            self.date_updated = timezone.now()
        else:
            self.date_created = timezone.now()
        return super(Well_Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.well_name

    #"recently" is being defined as within 1 day of "now"
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_updated <= now

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_created <= now

    pass

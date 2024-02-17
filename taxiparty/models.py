from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class TaxiParty(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today)
    time = models.TimeField(blank=False, default=datetime.time(8, 00))
    route = models.TextField(blank=False, default="wa mart to pt st")
    rider = models.TextField(blank=False, default="sangjun")


class route():
    origin = models.TextField(blank=False)
    destination = models.TextField(blank=False)
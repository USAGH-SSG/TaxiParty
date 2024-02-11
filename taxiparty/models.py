from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class TaxiParty(models.Model):
    date = models.DateTimeField(blank=False, default=timezone.now())
    route = models.TextField(blank=False, default="wa mart to pt st")
    rider = models.TextField(blank=False, default="sangjun")


class route():
    origin = models.TextField(blank=False)
    destination = models.TextField(blank=False)
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Location(models.Model):
    name = models.TextField(blank=False, unique=True)

class Route(models.Model):
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='route_origin')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='route_destination')
    
class TaxiParty(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today)
    time = models.TimeField(blank=False, default=datetime.time(8, 00))
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    rider = models.ManyToManyField(User)

    def getAbsoluteUrl(self):
        return reverse("taxiparty:taxipartydynamic", kwargs={"id": self.id})

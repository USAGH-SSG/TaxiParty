from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

# Create your models here.
class TaxiParty(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today)
    time = models.TimeField(blank=False, default=datetime.time(8, 00))
    route = models.TextField(blank=False)
    rider = models.TextField(blank=False)

    def getAbsoluteUrl(self):
        return reverse("taxiparty:taxipartydynamic", kwargs={"id": self.id})


class Route():
    origin = models.TextField(blank=False)
    destination = models.TextField(blank=False)

class Rider():
    rider1 = models.TextField(blank=False)
    rider2 = models.TextField()
    rider3 = models.TextField()
    rider4 = models.TextField()
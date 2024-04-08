from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

# Create your models here.
class Location(models.Model):
    name = models.TextField(blank=False, unique=True)

    def __str__(self) -> str:
        return self.name

# class Route(models.Model):
#     origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='route_origin')
#     destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='route_destination')

#     def __str__(self) -> str:
#         return self.origin.__str__() + " -> " + self.destination.__str__()
    
class TaxiParty(models.Model):
    date = models.DateField(blank=False, default=datetime.date.today)
    time = models.TimeField(blank=False, default=datetime.time(8, 00))
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination')
    rider = models.ManyToManyField(User, related_name='rider')
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='owner')

    def clean(self):
        if self.origin == self.destination:
            raise ValidationError("Origin and destination cannot be identical")

    def getAbsoluteUrl(self):
        return reverse("taxiparty:taxipartydynamic", kwargs={"id": self.id})

    def riderInStr(self):
        riders = ""
        for rider in self.rider.all():
            riders += str(rider) + ", "
        return riders[:-2]

    def __str__(self) -> str:
        return f"{self.origin} -> {self.destination}, {self.time.__str__()[:5]} {self.date.__str__()}."


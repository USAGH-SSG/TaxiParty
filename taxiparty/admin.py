from django.contrib import admin
from .models import TaxiParty, Location

# Register your models here.
admin.site.register(Location)
admin.site.register(TaxiParty)
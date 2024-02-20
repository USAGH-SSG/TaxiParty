from django.contrib import admin
from .models import TaxiParty, Location, Route

# Register your models here.
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(TaxiParty)
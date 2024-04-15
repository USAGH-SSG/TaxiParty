from django import forms

from .models import TaxiParty, Location

class TaxiPartyForm(forms.ModelForm):
    class Meta:
        model = TaxiParty
        fields = [
            'date',
            'time',
            'origin',
            'destination',

        ]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name'
        ]

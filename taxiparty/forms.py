from django import forms

from .models import TaxiParty

class TaxiPartyForm(forms.ModelForm):
    class Meta:
        model = TaxiParty
        fields = [
            'date',
            'time',
            'route',
            'rider',
        ]
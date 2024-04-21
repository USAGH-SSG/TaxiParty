from django import forms

from .models import TaxiParty, Location

class TaxiPartyForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': "form-control"
            }
        )
    )

    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': "form-control"
            }
        )
    )

    origin = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(
            attrs={
                'class': "form-select form-control"
            }
        )
    )

    destination = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(
            attrs={
                'class': "form-select form-control"
            }
        )
    )

    class Meta:
        model = TaxiParty
        fields = [
            'date',
            'time',
            'origin',
            'destination',
        ]

    def save(self, commit=True):
        instance = super(TaxiPartyForm, self).save(commit=False)
        instance.origin = self.cleaned_data['origin']
        instance.destination = self.cleaned_data['destination']
        if commit:
            instance.save()
        return instance

class LocationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': "form-control"
            }
        )
    )
    
    class Meta:
        model = Location
        fields = [
            'name'
        ]

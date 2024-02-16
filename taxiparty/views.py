from django.shortcuts import render
from django.http import HttpResponse

from .models import TaxiParty
from .forms import TaxiPartyForm

# Create your views here.
def createTaxiParty_view(request):
    form = TaxiPartyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaxiPartyForm()
    
    context = {
        'form': form
    }
    return render(request, "createtaxiparty.html", context)

def home_view(request):
    partyList = TaxiParty.objects.all()
    print(partyList)
    
    context = {
        "partyList": partyList
    }
    return render(request, "taxipartyhome.html", context)
from django.shortcuts import render, get_object_or_404, redirect
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

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    context = {
        "party": obj
    }
    return render(request, "partydetail.html", context)

def party_delete_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {
        "party": obj
    }
    return render(request, "delete_party.html", context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import TaxiParty, Location, Route
from .forms import TaxiPartyForm, LocationForm, RouteForm

# Create your views here.
def createTaxiParty_view(request):
    form = TaxiPartyForm(request.POST or None)
    if form.is_valid():
        party = form.save()
        party.rider.add(request.user)
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={"id": party.id}))
    
    context = {
        'form': form
    }
    return render(request, "createtaxiparty.html", context)

def create_location_view(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('taxiparty:home'))
    
    context = {
        'form': form
    }
    return render(request, "create_location.html", context)

def create_route_view(request):
    form = RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('taxiparty:home'))
    
    context = {
        'form': form
    }
    return render(request, "create_route.html", context)

def home_view(request):
    partyList = TaxiParty.objects.all()
    
    context = {
        "partyList": partyList
    }
    return render(request, "taxipartyhome.html", context)

def view_location_view(request):
    locationList = Location.objects.all()
    
    context = {
        "locationList": locationList
    }
    return render(request, "view_location.html", context)

def view_route_view(request):
    routeList = Route.objects.all()
    
    context = {
        "routeList": routeList
    }
    return render(request, "view_route.html", context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    joinable = (request.user not in obj.rider.all())
    anon = request.user.is_anonymous
    print(request.user)
    context = {
        "party": obj,
        "joinable": joinable,
        "anon": anon
    }
    return render(request, "partydetail.html", context)

def party_delete_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('taxiparty:home'))
    context = {
        "party": obj
    }
    return render(request, "delete_party.html", context)

def party_edit_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    if request.method == 'POST':    
        form = TaxiPartyForm(request.POST)
        if form.is_valid():
            obj.delete()
            party = form.save()
            return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': party.id}))
    else:
        form = TaxiPartyForm(instance=obj)
    context = {
        'form': form
    }
    return render(request, 'edit_party.html', context)

def party_join_view(request, id):
    joiner = request.user
    TaxiParty.objects.get(id=id).rider.add(joiner)
    return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))
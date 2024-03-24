from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import TaxiParty, Location
from .forms import TaxiPartyForm, LocationForm    

# Create your views here.
def createTaxiParty_view(request):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
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
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('taxiparty:home'))
    
    context = {
        'form': form
    }
    return render(request, "create_location.html", context)

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

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    joinable = (request.user not in obj.rider.all())
    anon = request.user.is_anonymous
    context = {
        "party": obj,
        "joinable": joinable,
        "anon": anon
    }
    return render(request, "partydetail.html", context)

def party_edit_view(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    obj = get_object_or_404(TaxiParty, id=id)
    if request.method == 'POST':    
        form = TaxiPartyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))
    else:
        form = TaxiPartyForm(instance=obj)
    context = {
        'form': form
    }
    return render(request, 'edit_party.html', context)

def party_join_view(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    joiner = request.user
    obj = get_object_or_404(TaxiParty, id=id)
    obj.rider.add(joiner)
    return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))

def party_leave_view(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    obj = get_object_or_404(TaxiParty, id=id)
    riders = obj.rider.all()
    print(riders)
    if request.user not in riders:
        messages.info(request, 'You are not part of the Taxi Party!')
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))
    else:
        leavingUser = request.user
        obj.rider.remove(leavingUser)
        return redirect(reverse('taxiparty:home'))
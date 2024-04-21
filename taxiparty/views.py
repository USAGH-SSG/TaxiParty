from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import TaxiParty, Location
from .forms import TaxiPartyForm, LocationForm
from .serializers import TaxiPartySerializer

import datetime

# Create your views here.
def createTaxiParty_view(request):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    form = TaxiPartyForm(request.POST or None)

    # if request.method == 'POST':
    if form.is_valid():
        party = form.save()
        party.rider.add(request.user)
        party.owner = request.user
        party.save()
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={"id": party.id}))
    
    locations = Location.objects.all()

    context = {
        'form': form,
        'locations': locations,
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
    if request.user != obj.owner:
        messages.info(request, 'You are not the owner of the Taxi Party!')
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))
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
    if obj.owner == None:
        obj.owner = joiner
    obj.save()
    return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))

def party_leave_view(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    obj = get_object_or_404(TaxiParty, id=id)
    riders = obj.rider.all()
    if request.user not in riders:
        messages.info(request, 'You are not part of the Taxi Party!')
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={'id': id}))
    else:
        leavingUser = request.user
        obj.rider.remove(leavingUser)
        riders = obj.rider.all()
        if obj.owner == leavingUser and len(obj.rider.all()) == 0:
            obj.owner = None
        elif obj.owner == leavingUser:
            obj.owner = riders[0]
        obj.save()
        return redirect(reverse('taxiparty:home'))

def my_party_view(request):
    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    myParties = TaxiParty.objects.filter(rider=request.user)
    context = {
        'partyList': myParties
    }
    return render(request, "myparty.html", context)
    
def daily_party_view(request, date: str):
    try:
        year, month, day = [int(x) for x in date.split('-')]
        dateInDateTime = datetime.date(year, month, day)
        myParties = TaxiParty.objects.filter(date=dateInDateTime)
        context = {
            'date': dateInDateTime.__str__(),
            'partyList': myParties
        }
    except:
        messages.info(request, 'Oops! Wrong Date Entered! Please enter a valid date.')
        context = {
            'partyList': []
        }

    return render(request, "dailyparty.html", context)

@api_view(['GET'])
def getTaxiPartyOfMonth(request):
    givenMonth = str(3)

    if len(givenMonth) == 1:
        givenMonth = '0' + givenMonth
    givenMonth = f"-{givenMonth}-"

    party = TaxiParty.objects.all().filter(date__contains=givenMonth)
    serializer = TaxiPartySerializer(party, many=True)
    return Response(serializer.data)
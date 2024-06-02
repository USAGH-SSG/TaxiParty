from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import Http404
from django_user_agents.utils import get_user_agent

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import TaxiParty, Location
from .forms import TaxiPartyForm, LocationForm
from .serializers import TaxiPartySerializer

import datetime
import time

# Create your views here.
def createTaxiParty_view(request):
    user_agent = get_user_agent(request)

    if request.user.is_anonymous:
        return redirect(reverse('user:login'))
    form = TaxiPartyForm(request.POST or None)

    # if request.method == 'POST':
    if form.is_valid():
        party = form.save()
        print(party.time)
        party.rider.add(request.user)
        party.owner = request.user
        party.save()
        return redirect(reverse('taxiparty:taxipartydynamic', kwargs={"id": party.id}))

    locations = Location.objects.all()

    context = {
        'mobile': user_agent.is_mobile,
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
    user_agent = get_user_agent(request)

    context = {
        'form': form,
        'mobile': user_agent.is_mobile
    }
    return render(request, "create_location.html", context)

def home_view(request):
    user_agent = get_user_agent(request)

    context = {
        'mobile': user_agent.is_mobile
    }

    if user_agent.is_mobile:
        return render(request, "mobile_taxipartyhome.html", context)
    elif user_agent.is_pc:
        return render(request, "taxipartyhome.html", context)



def view_location_view(request):
    locationList = Location.objects.all()
    user_agent = get_user_agent(request)

    context = {
        "locationList": locationList,
        'mobile': user_agent.is_mobile
    }
    return render(request, "view_location.html", context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(TaxiParty, id=id)
    joinable = (request.user not in obj.rider.all())
    editable = (request.user == obj.owner)
    anon = request.user.is_anonymous
    user_agent = get_user_agent(request)

    context = {
        "party": obj,
        "editable": editable,
        "joinable": joinable,
        "anon": anon,
        'mobile': user_agent.is_mobile
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

    user_agent = get_user_agent(request)
    
    context = {
        'form': form,
        'mobile': user_agent.is_mobile
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
    user_agent = get_user_agent(request)

    context = {
        'mobile': user_agent.is_mobile,
        'partyList': myParties
    }
    return render(request, "myparty.html", context)

def daily_party_view(request, date: str):
    user_agent = get_user_agent(request)

    try:
        year, month, day = [int(x) for x in date.split('-')]
        dateInDateTime = datetime.date(year, month, day)
        myParties = TaxiParty.objects.filter(date=dateInDateTime)
        context = {
            'date': dateInDateTime.__str__(),
            'partyList': myParties,
            'mobile': user_agent.is_mobile
        }
    except:
        messages.info(request, 'Oops! Wrong Date Entered! Please enter a valid date.')
        context = {
            'mobile': user_agent.is_mobile,
            'partyList': []
        }

    return render(request, "dailyparty.html", context)

def party_delete_view(request, id):
    if request.user.is_anonymous or not request.user.is_superuser:
        raise Http404
    party = get_object_or_404(TaxiParty, id=id)
    party.delete()
    return redirect(reverse('taxiparty:home'))


# @api_view(['REMOVE'])

@api_view(['GET'])
def getTaxiPartyOfMonth(request, yearMonth):
    try:
        testYearMonth = str(yearMonth)
        testYearMonth += "-01"
        format = "%Y-%m-%d"
        time.strptime(testYearMonth, format)
    except:
        raise Http404
    party = TaxiParty.objects.all().filter(date__contains=str(yearMonth))
    serializer = TaxiPartySerializer(party, many=True)
    return Response(serializer.data)

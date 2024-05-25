import pytest    
import datetime

from .models import TaxiParty, Location
from user.models import User

# Create your tests here.

@pytest.mark.django_db #give test access to database
def test_location_create():    
    # Create dummy data
    location = Location.objects.create(
        name = "testLocation"
        )
    assert location.name=="testLocation"

@pytest.mark.django_db #give test access to database
def test_taxiparty_create():
    loc1 = Location.objects.create(
        name = "testLocation1"
        )

    loc2 = Location.objects.create(
        name = "testLocation2"
        )

    user = User.objects.create(
        username = "testaccount",
        name = "testacc",
    )
    
    taxiParty = TaxiParty.objects.create(
        date=datetime.date.today(), 
        time=datetime.time(8,0),  
        origin=loc1,
        destination=loc2,
        owner=user
        )
    taxiParty.rider.add(user)
    taxiParty.save()
    # Assert the dummy data saved as expected       
    assert taxiParty.date==datetime.date.today()
    assert taxiParty.time==datetime.time(8,0)
    assert taxiParty.origin==loc1
    assert taxiParty.destination==loc2
    assert list(taxiParty.rider.all())==list(User.objects.filter(id=user.id))
    assert taxiParty.owner==user

    user2 = User.objects.create(
        username = "testaccount2",
        name = "testacc2",
    )
    taxiParty.rider.add(user2)
    taxiParty.save()
    assert list(taxiParty.rider.all())==list(User.objects.all())

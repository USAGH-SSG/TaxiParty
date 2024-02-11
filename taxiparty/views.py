from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def createTaxiParty_view(request):
    print(request)
    return render(request, "createtaxiparty.html")

def home_view(request):
    return render(request, "taxipartyhome.html")
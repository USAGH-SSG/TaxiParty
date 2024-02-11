from django.urls import path
from . import views

# url config
urlpatterns = [
    path('createtaxiparty/', views.createTaxiParty_view),
    path('home/', views.home_view)
]
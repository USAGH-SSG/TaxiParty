from django.urls import path
from . import views

# url config
urlpatterns = [
    path('', views.home_view),
    path('createtaxiparty/', views.createTaxiParty_view),
]
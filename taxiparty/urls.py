from django.urls import path
from . import views

# url config
urlpatterns = [
    path('', views.home_view),
    path('createtaxiparty/', views.createTaxiParty_view),
    path('taxiparty/<int:id>/', views.dynamic_lookup_view),
    path('taxiparty/<int:id>/delete/', views.party_delete_view)
]
from django.urls import path
from . import views

# url config
app_name = 'taxiparty'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('createtaxiparty/', views.createTaxiParty_view, name='createtaxiparty'),
    path('taxiparty/<int:id>/', views.dynamic_lookup_view, name='taxipartydynamic'),
    path('taxiparty/<int:id>/edit/', views.party_edit_view, name='taxipartyedit'),
    path('taxiparty/<int:id>/join/', views.party_join_view, name='taxipartyjoin'),
    path('taxiparty/<int:id>/leave/', views.party_leave_view, name='taxipartyleave'),

    path('taxiparty/daily/<slug:date>/', views.daily_party_view, name='dailyparty'),
    path('taxiparty/month/<slug:month>', views.getTaxiPartyOfMonth, name='monthlytaxiparty'),

    path('createlocation/', views.create_location_view, name='createlocation'),
    path('viewlocation/', views.view_location_view, name='viewlocation'),
    path('myparty/', views.my_party_view, name='myparty'),
]
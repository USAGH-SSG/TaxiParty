from django.urls import path
from . import views

# url config
app_name = 'taxiparty'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('createtaxiparty/', views.createTaxiParty_view, name='createtaxiparty'),
    path('taxiparty/<int:id>/', views.dynamic_lookup_view, name='taxipartydynamic'),
    path('taxiparty/<int:id>/delete/', views.party_delete_view, name='taxipartydelete'),
    path('taxiparty/<int:id>/edit/', views.party_edit_view, name='taxipartyedit'),
    path('taxiparty/<int:id>/join/', views.party_join_view, name='taxipartyjoin'),

    path('createlocation/', views.create_location_view, name='createlocation'),
    path('viewlocation/', views.view_location_view, name='viewlocation'),
    # path('createroute/', views.create_route_view, name='createroute'),
    # path('viewroute/', views.view_route_view, name='viewroute'),
]
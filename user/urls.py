from django.urls import path
from . import views

# url config
app_name = 'user'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    # path('', views.home_view, name='home'),
    # path('createtaxiparty/', views.createTaxiParty_view, name='taxipartyview'),
    # path('taxiparty/<int:id>/', views.dynamic_lookup_view, name='taxipartydynamic'),
    # path('taxiparty/<int:id>/delete/', views.party_delete_view, name='taxipartydelete'),
    # path('taxiparty/<int:id>/edit/', views.party_edit_view, name='taxipartyedit')
]
from rest_framework import serializers
from .models import TaxiParty
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TaxiPartySerializer(serializers.ModelSerializer):
    origin_name = serializers.ReadOnlyField(source='origin.name')
    destination_name = serializers.ReadOnlyField(source='destination.name')
    owner_name = serializers.ReadOnlyField(source='owner.username')
    rider = UserSerializer(read_only=True, many=True)

    class Meta:
        model = TaxiParty
        fields = ('id', 'date', 'time','origin_name','destination_name', 'owner_name', 'rider')


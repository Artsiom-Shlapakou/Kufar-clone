from rest_framework import serializers
from locations.models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = (
            'id', 
            'name'
        )


class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = (
            'id', 
            'name', 
            'country'
        )

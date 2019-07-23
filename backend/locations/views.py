from rest_framework import viewsets
from locations.models import City, Country
from locations.serializers import CountrySerializer, CitySerializer
from locations.pagination import LocationsResultSetPagination

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = LocationsResultSetPagination


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = LocationsResultSetPagination


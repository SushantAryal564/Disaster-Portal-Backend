import django_filters
from models import *

class AmenitiesFilter(django_filters.FilterSet):
    fclass = django_filters.CharFilter(field_name='fclass')

    class Meta:
        model = Amenities
        fields = ['fclass']
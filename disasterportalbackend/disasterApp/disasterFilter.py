import django_filters
from .models import *

class DisasterTimeFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    end_time = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = DisasterEvent
        fields = ['startTime', 'expireTime']
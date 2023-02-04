import django_filters
from rest_framework import viewsets
from .models import DisasterEvent

class DisasterFilter(django_filters.FilterSet):
    class Meta:
        model = DisasterEvent
        fields = ["name", "ward","type"]
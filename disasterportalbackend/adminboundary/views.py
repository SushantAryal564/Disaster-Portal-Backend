from rest_framework import viewsets
from .models import *
from .serializer import *
class LalitpurMetroViewSet(viewsets.ModelViewSet):
    queryset = LalitpurMetro.objects.all()
    serializer_class = LalitpurMetroSerializer
class WardWithGeomViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardWithoutGeomSerializer
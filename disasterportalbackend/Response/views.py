from rest_framework import viewsets
from .models import *
class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = UserSerializer
  
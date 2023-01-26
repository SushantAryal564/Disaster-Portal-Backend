from rest_framework import viewsets

from .models import *
from .serializers import *
from .permission import *
class ClusterTypeViewSet(viewsets.ModelViewSet):
  queryset = ClusterType.objects.all()
  permission_classes = [OnlyGet,]
  serializer_class = ClusterTypeSerializer

class RatingViewSet(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  permission_classes = [OnlyGet,]
  serializer_class = RatingSerializer

class DisasterTypeViewSet(viewsets.ModelViewSet):
  queryset = DisasterType.objects.all()
  permission_classes = [OnlyGet,]
  serializer_class = DisasterTypeSerializer

class DisasterEventViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  permission_classes = [DisasterEventPermission,]
  serializer_class = DisasterEventSerializer
  def perform_create(self, serializer):
    if self.request.user.is_authenticated:
      if(self.request.user.username):
        source = self.request.user.username;
      else:
        source = "unknown"
      serializer.save(is_verified=True,source=source)



from rest_framework import viewsets
from django.contrib.gis.geos import GEOSGeometry
from django_filters import rest_framework as filters
from rest_framework  import filters as rest_filters
from .disasterFilter import *
# from .filter import *
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
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  filter_class = DisasterTimeFilter
  filterset_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  search_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  
  def perform_create(self, serializer):
    source = "unknown"
    if self.request.user.is_authenticated:
      if(self.request.user.username):
        source = self.request.user.username;
    lat = self.request.data['lat']
    lng = self.request.data['long']
    pntString = "POINT"+"("+lng+" "+lat+")"
    pnt = GEOSGeometry(pntString)
    serializer.save(is_verified=True,source=source,geom = pnt)

class DisasterEventWithoutGeomViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  permission_classes = [DisasterEventPermission,]
  serializer_class = DisasterEventWitoutWardGeomSerializer
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  filter_class = DisasterTimeFilter
  filterset_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  search_fields = ['name','Ward','type','is_closed','startTime','expireTime']

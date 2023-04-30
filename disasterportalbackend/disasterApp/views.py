from rest_framework import viewsets
from django.contrib.gis.geos import GEOSGeometry
from django_filters import rest_framework as filters
from rest_framework  import filters as rest_filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
# from .disasterFilter import *
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
  authentication_classes = [JWTAuthentication]
  serializer_class = DisasterEventSerializer
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  # filterset_class = DisasterTimeFilter
  # filterset_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  filterset_fields = {
    'name':['exact'],
    'Ward':['exact'],
    'type':['exact'],
    'is_closed':['exact'],
    'startTime':['gte', 'gt', 'lt'],
  }
  search_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  
  def perform_create(self, serializer):
    source = "unknown"
    is_verified=False
    if self.request.user.is_authenticated:
      if(self.request.user.username):
        source = self.request.user.username;
        is_verified=True
    lat = self.request.data['lat']
    lng = self.request.data['long']
    pntString = "POINT"+"("+lng+" "+lat+")"
    pnt = GEOSGeometry(pntString)
    serializer.save(is_verified=is_verified,source=source,geom = pnt)

class DisasterEventWithoutGeomViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  permission_classes = [DisasterEventPermission,]
  authentication_classes = [JWTAuthentication]
  serializer_class = DisasterEventWitoutWardGeomSerializer
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  filterset_fields = {
    'name':['exact'],
    'Ward':['exact'],
    'type':['exact'],
    'is_closed':['exact'],
    'startTime':['gte', 'gt','exact', 'lte'],
  }
  search_fields = ['name','Ward','type','is_closed','startTime','expireTime']



class DisasterEventTypeModifiedViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  permission_classes = [DisasterEventPermission,]
  authentication_classes = [JWTAuthentication]
  serializer_class = DisasterEventSerializerTypeModified
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  

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

class DisasterEventChartInformationViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  serializer_class = DisasterEventChartInformationSerializer
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  filterset_fields = {
    'Ward':['exact'],
    'is_closed':['exact'],
    'startTime':['gte','lte'],
  }
  search_fields = ['Ward','is_closed','startTime','is_closed']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DisasterEventSerializerTypeModified
from .models import DisasterEvent



@api_view(['PATCH'])
def update_disaster_event(request, pk):
    try:
        event = DisasterEvent.objects.get(pk=pk)
    except DisasterEvent.DoesNotExist:
        return Response({'error': 'Disaster event not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DisasterEventSerializerTypeModified(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import DisasterEvent

class DownloadCSV(APIView):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="disaster_events.csv"'

        # Get the query parameters
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        disaster_type = request.GET.get('disaster_type')
        events = DisasterEvent.objects.all()
        print(start_date, end_date,disaster_type)
        if start_date:
          start_date = timezone.make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
          events = events.filter(date_event__gte=start_date)
          print(events);
        if disaster_type:
            events = events.filter(type__title=disaster_type)
            print(events);
        writer = csv.writer(response)
        writer.writerow(['Name', 'Ward', 'Latitude', 'Longitude', 'Date of Event', 'Date Closed', 'Registered Date', 'Update Date', 'Is Verified', 'Is Closed', 'Disaster Type', 'Rating', 'Source', 'Description', 'Start Time', 'Expire Time', 'People Death', 'Estimated Loss', 'Infrastructure Destroyed'])

        for event in events:
            writer.writerow([event.name, event.Ward.ward, event.lat, event.long, event.date_event, event.date_closed, event.registered_date, event.update_date, event.is_verified, event.is_closed, event.type, event.rating, event.source, event.description, event.startTime, event.expireTime, event.peopleDeath, event.estimatedLoss, event.InfrastructureDestroyed])

        return response
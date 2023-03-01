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
  authentication_classes = [JWTAuthentication]
  serializer_class = DisasterEventWitoutWardGeomSerializer
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  # filterset_class = DisasterTimeFilter
  filterset_fields = {
    'name':['exact'],
    'Ward':['exact'],
    'type':['exact'],
    'is_closed':['exact'],
    'startTime':['gte', 'gt','exact', 'lte'],
  }
  search_fields = ['name','Ward','type','is_closed','startTime','expireTime']
  
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
          print(start_date,"((((((((((((((((()))))))))))))))))")
          events = events.filter(date_event__gte=start_date)
          print("Second query:**************")
          print(events);
        if disaster_type:
            events = events.filter(type__title=disaster_type)
            print("Fourth query:**************")
            print(events);
        # Write the CSV file
        writer = csv.writer(response)
        writer.writerow(['Name', 'Ward', 'Latitude', 'Longitude', 'Date of Event', 'Date Closed', 'Registered Date', 'Update Date', 'Is Verified', 'Is Closed', 'Disaster Type', 'Rating', 'Source', 'Description', 'Start Time', 'Expire Time', 'People Death', 'Estimated Loss', 'Infrastructure Destroyed'])

        for event in events:
            writer.writerow([event.name, event.Ward.ward, event.lat, event.long, event.date_event, event.date_closed, event.registered_date, event.update_date, event.is_verified, event.is_closed, event.type, event.rating, event.source, event.description, event.startTime, event.expireTime, event.peopleDeath, event.estimatedLoss, event.InfrastructureDestroyed])

        return response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DisasterEvent
from datetime import datetime, timedelta
import shapefile

class DownloadShapefile(APIView):
    def get(self, request):
        # Get parameters from request
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        disaster_type = request.GET.get('disaster_type')

        # Filter events based on parameters
        events = DisasterEvent.objects.all()
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            events = events.filter(date_event__gte=start_date)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
            events = events.filter(date_event__lte=end_date)
        if disaster_type:
            events = events.filter(type__name=disaster_type)

        # Create shapefile
        sf = shapefile.Writer('disaster_events')
        sf.field('Name', 'C', '40')
        sf.field('Ward', 'N', '10')
        sf.field('Latitude', 'F', '10', 8)
        sf.field('Longitude', 'F', '10', 8)
        sf.field('Date of Event', 'C', '20')
        sf.field('Date Closed', 'C', '20')
        sf.field('Registered Date', 'C', '20')
        sf.field('Update Date', 'C', '20')
        sf.field('Is Verified', 'L')
        sf.field('Is Closed', 'L')
        sf.field('Disaster Type', 'C', '20')
        sf.field('Rating', 'C', '10')
        sf.field('Source', 'C', '50')
        sf.field('Description', 'C', '250')
        sf.field('Start Time', 'C', '20')
        sf.field('Expire Time', 'C', '20')
        sf.field('People Death', 'N', '10')
        sf.field('Estimated Loss', 'F', '20', 2)
        sf.field('Infrastructure Destroyed', 'N', '10')

        for event in events:
            sf.point(event.long, event.lat)
            sf.record(event.name, event.Ward.ward, event.lat, event.long, str(event.date_event), str(event.date_closed), str(event.registered_date), str(event.update_date), event.is_verified, event.is_closed, event.type.name, event.rating, event.source, event.description, str(event.startTime), str(event.expireTime), event.peopleDeath, event.estimatedLoss, event.InfrastructureDestroyed)

        # Create response
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="disaster_events.zip"'

        # Save shapefile to response
        with shapefile.WriterZip(response) as zipwriter:
            zipwriter.add_file('disaster_events.shp', sf)
            zipwriter.add_file('disaster_events.dbf', sf)
            zipwriter.add_file('disaster_events.shx', sf)
        return response

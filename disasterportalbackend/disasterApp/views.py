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

class DisasterEventTypeModifiedViewSet(viewsets.ModelViewSet):
  queryset = DisasterEvent.objects.all()
  permission_classes = [DisasterEventPermission,]
  authentication_classes = [JWTAuthentication]
  serializer_class = DisasterEventSerializerTypeModified
  filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
  
  # def create(self, request, *args, **kwargs):
  #   print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
  #   print(request.data) 
  
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

# from django.http import HttpResponse
# from django.views.generic import View
# from shp.views import send_shapefile_response
# from .models import DisasterEvent
# import datetime

# class DownloadShapefile(View):
#     def get(self, request):
#         start_date_str = request.GET.get('start_date', None)
#         end_date_str = request.GET.get('end_date', None)
#         disaster_type_str = request.GET.get('disaster_type', None)

#         if start_date_str and end_date_str:
#             start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
#             end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d') + datetime.timedelta(days=1)
#             events = DisasterEvent.objects.filter(date_event__range=(start_date, end_date))
#         else:
#             events = DisasterEvent.objects.all()

#         if disaster_type_str:
#             events = events.filter(type__name=disaster_type_str)

#         fields = [
#             ('Name', 'string', 50),
#             ('Ward', 'int', 10),
#             ('Latitude', 'float', 20),
#             ('Longitude', 'float', 20),
#             ('Date of Event', 'date'),
#             ('Date Closed', 'date'),
#             ('Registered Date', 'date'),
#             ('Update Date', 'date'),
#             ('Is Verified', 'bool'),
#             ('Is Closed', 'bool'),
#             ('Disaster Type', 'string', 50),
#             ('Rating', 'int', 10),
#             ('Source', 'string', 50),
#             ('Description', 'string', 255),
#             ('Start Time', 'datetime'),
#             ('Expire Time', 'datetime'),
#             ('People Death', 'int', 10),
#             ('Estimated Loss', 'float', 20),
#             ('Infrastructure Destroyed', 'int', 10)
#         ]

#         data = []
#         for event in events:
#             row = []
#             row.append(event.name)
#             row.append(event.Ward.ward)
#             row.append(event.lat)
#             row.append(event.long)
#             row.append(event.date_event)
#             row.append(event.date_closed)
#             row.append(event.registered_date)
#             row.append(event.update_date)
#             row.append(event.is_verified)
#             row.append(event.is_closed)
#             row.append(event.type.name)
#             row.append(event.rating)
#             row.append(event.source)
#             row.append(event.description)
#             row.append(event.startTime)
#             row.append(event.expireTime)
#             row.append(event.peopleDeath)
#             row.append(event.estimatedLoss)
#             row.append(event.InfrastructureDestroyed)
#             data.append(row)

#         return send_shapefile_response('disaster_events', fields, data)
from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'clusterType',ClusterTypeViewSet)
router.register(r'rating',RatingViewSet)
router.register(r'disasterType',DisasterTypeViewSet)
router.register(r'disasterEvent',DisasterEventViewSet)
router.register(r'disasterEventwithoutgeom',DisasterEventWithoutGeomViewSet)
# router.register(r'test',TestDisasterEventWithoutGeomViewSet)
urlpatterns = [
    
  path('', include(router.urls)),
  path('download-csv/', DownloadCSV.as_view(), name='download-csv'),
  path('download-shp/', getShapefile.as_view(), name='download-shp'),
   path('geoserver-data/', geoserver_data, name='geoserver-data'),

]
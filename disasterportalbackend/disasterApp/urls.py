from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'clusterType',ClusterTypeViewSet)
router.register(r'rating',RatingViewSet)
router.register(r'disasterType',DisasterTypeViewSet)
router.register(r'disasterEvent',DisasterEventViewSet)
urlpatterns = [
  path('', include(router.urls)),
]
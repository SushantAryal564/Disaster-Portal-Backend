from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'lalitpurMetro', LalitpurMetroViewSet)
router.register(r'ward',WardViewSet)
urlpatterns = [
  path('', include(router.urls)),
]
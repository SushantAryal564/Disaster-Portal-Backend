from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'lalitpurMetro', LalitpurMetroViewSet)
router.register(r'ward',WardWithGeomViewSet)
urlpatterns = [
  path('', include(router.urls)),
  path('wards/<int:ward_number>/', WardDetail.as_view()),
]
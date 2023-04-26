from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'lalitpurMetro', LalitpurMetroViewSet)
router.register(r'ward',WardWithGeomViewSet)
router.register(r'chartward',ChartInformationViewSet)
urlpatterns = [
  path('', include(router.urls)),
  path('wards/<int:ward_number>/', WardDetail.as_view()),
  path("getward/",GetWardFromLatlng.as_view()),
  
]
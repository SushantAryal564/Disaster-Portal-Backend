from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from SpatialAnalysis.views import *
router = routers.DefaultRouter()
router.register(r'allbuilding', BuildingViewset)
router.register(r'amenites',AmenitiesViewset)
urlpatterns = [
    path('', include(router.urls)),
    path("building/", BufferPolygonIntersectionViewBuilding.as_view()),
    path("forest/",BufferPolygonIntersectionViewForest.as_view()),
    path("waterbody/",BufferPolygonIntersectionViewWaterBody.as_view()),
    path("amenities/",BufferPolygonIntersectionViewAmenities.as_view()),
    path('nearest_amenities/<str:latitude>/<str:longitude>/<int:distance>/', NearestAmenities.as_view()),
    path('nearest_buildings/<str:latitude>/<str:longitude>/<int:distance>/', NearestBuildings.as_view()),
    path('nearest_forests/<str:latitude>/<str:longitude>/<int:distance>/', NearestForests.as_view()),
    path('nearest_roads/<str:latitude>/<str:longitude>/<int:distance>/', NearestRoads.as_view()),
    path('nearest_waterbody/<str:latitude>/<str:longitude>/<int:distance>/', NearestWaterBody.as_view()),
    path('singlebuilding/',SingleBuildingViewset.as_view(),name='single-building'),
    path('email/',BufferPolygonIntersectionViewBuildingTriggerAlert.as_view(),name='alert-email'),
    path('patchbuilding/', building_partial_update,name='patch building'),
    path('download_building/',download_building_event),
      path('download_disaster/',download_disaster_event)
]
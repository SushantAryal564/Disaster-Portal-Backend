from django.contrib import admin
from django.urls import path,include

from SpatialAnalysis.views import *

urlpatterns = [
    path("building/", BufferPolygonIntersectionViewBuilding.as_view()),
    path("forest/",BufferPolygonIntersectionViewForest.as_view()),
    path("waterbody/",BufferPolygonIntersectionViewWaterBody.as_view()),
    path("amenities/",BufferPolygonIntersectionViewAmenities.as_view()),
    path('nearest_amenities/<str:latitude>/<str:longitude>/', NearestAmenities.as_view(), name='nearest_amenities'),

]
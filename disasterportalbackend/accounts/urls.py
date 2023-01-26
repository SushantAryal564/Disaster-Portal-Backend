from rest_framework import routers
from django.urls import path, include
from .views import *

urlpatterns = [
  path('login',LoginAPI.as_view())
]
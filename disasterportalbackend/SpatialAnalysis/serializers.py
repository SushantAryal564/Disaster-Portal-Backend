from rest_framework import serializers
from .models import *

class AmenitiesSerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Metal:
    model: Amenities
    fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Metal:
    model: Buildings
    fields = '__all__'

class ForestSerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Metal:
    model: Forest
    fields = '__all__'

class WaterBodySerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Metal:
    model: Waterbody
    fields = '__all__'

class RoadSerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Metal:
    model: Road
    fields = '__all__'
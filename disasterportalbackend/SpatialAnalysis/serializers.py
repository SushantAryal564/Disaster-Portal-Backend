from rest_framework import serializers
from .models import *

class AmenitiesSerializer(serializers.ModelSerializer):
  class Meta:
    model: Amenities
    fields = '__all__'

class BuildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = '__all__'

class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = '__all__'

class WaterBodySerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Meta:
    model: Waterbody
    fields = '__all__'

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'
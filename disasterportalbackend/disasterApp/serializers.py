from rest_framework import serializers
from .models import *

class ClusterTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClusterType
    fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = '__all__'
    
class DisasterTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DisasterType
    fields = '__all__'

class DisasterEventSerializer(serializers.ModelSerializer):
  class Meta:
    model = DisasterEvent
    fields = '__all__'


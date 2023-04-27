from rest_framework import serializers
from .models import *
from adminboundary.serializer import *;
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
  type = DisasterTypeSerializer()
  class Meta:
    model = DisasterEvent
    exclude = ['geom', 'is_verified','is_closed']

class DisasterEventSerializerTypeModified(serializers.ModelSerializer):
  # type = DisasterTypeSerializer()
  class Meta:
    model = DisasterEvent
    fields = '__all__'

class DisasterEventWitoutWardGeomSerializer(serializers.ModelSerializer):
  type = DisasterTypeSerializer()
  Ward = WardWithoutGeomSerializer()
  class Meta:
    model = DisasterEvent
    exclude = ['geom', 'is_verified','is_closed']

class DisasterEventChartInformationSerializer(serializers.ModelSerializer):
  type = DisasterTypeSerializer()
  class Meta:
    model = DisasterEvent
    fields = ['startTime','Ward', 'peopleDeath','estimatedLoss','InfrastructureDestroyed','type','is_closed']
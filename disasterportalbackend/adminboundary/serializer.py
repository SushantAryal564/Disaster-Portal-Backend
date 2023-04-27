from rest_framework_gis.serializers import GeoFeatureModelSerializer;
from rest_framework import serializers
from .models import *;
class LalitpurMetroSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Lalitpurmetro
        geo_field = "geom"
        fields = '__all__'

class WardSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ward
        geo_field = "geom"
        fields = '__all__';

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ('ward', 'total_infrastructure_damaged', 'total_estimated_loss','total_people_death','number_of_disasters');

class WardWithoutGeomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        exclude = ['geom',];
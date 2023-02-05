from rest_framework_gis.serializers import GeoFeatureModelSerializer;
from rest_framework import serializers
from .models import *;
class LalitpurMetroSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LalitpurMetro
        geo_field = "geom"
        fields = '__all__'

class WardSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ward
        geo_field = "geom"
        fields = '__all__'

class WardWithoutGeomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        exclude = ['geom',];
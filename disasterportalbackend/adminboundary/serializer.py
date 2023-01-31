from rest_framework_gis.serializers import GeoFeatureModelSerializer
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
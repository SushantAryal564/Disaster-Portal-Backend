from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class AmenitiesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model: Amenities
        geo_field = 'geom'
        fields = '__all__'

class BuildingsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Buildings
        geo_field = 'geom'
        fields = '__all__'

class ForestSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Forest
        geo_field = 'geom'
        fields = '__all__'

class WaterBodySerializer(GeoFeatureModelSerializer):
    class Meta:
        model: Waterbody
        geo_field = 'geom'
        fields = '__all__'

class RoadSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'
from django.contrib.gis.db import models


class Amenities(models.Model):
    geom = models.PolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amenities'


class Buildings(models.Model):
    geom = models.PolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Buildings'


class Forest(models.Model):
    geom = models.PolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Forest'

class Waterbody(models.Model):
    geom = models.PolygonField(blank=True, null=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Waterbody'

class RoadLalitpur(models.Model):
    geom = models.LineStringField(blank=True, null=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)    
    tunnel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:        
      managed = False
      db_table = 'road_lalitpur'
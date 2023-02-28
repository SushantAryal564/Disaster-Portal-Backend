from django.contrib.gis.db import models


class Amenities(models.Model):
    gid = models.AutoField(primary_key=True)     
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amenities'


class Buildings(models.Model):
    gid = models.AutoField(primary_key=True)
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    ward = models.IntegerField(blank=True, null=True)
    phone_number_1 = models.CharField(max_length=10, blank=True, null=True)
    phone_number_2 = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=10, blank=True, null=True)
    housemetricnumber = models.CharField(max_length=50, blank=True, null=True)
    people = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Buildings'


class Forest(models.Model):
    gid = models.AutoField(primary_key=True)     
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Forest'


class Road(models.Model):
    gid = models.AutoField(primary_key=True)     
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    ref = models.CharField(max_length=20, blank=True, null=True)
    oneway = models.CharField(max_length=1, blank=True, null=True)
    maxspeed = models.SmallIntegerField(blank=True, null=True)
    layer = models.FloatField(blank=True, null=True)
    bridge = models.CharField(max_length=1, blank=True, null=True)
    tunnel = models.CharField(max_length=1, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Road'


class Waterbody(models.Model):
    gid = models.AutoField(primary_key=True)     
    osm_id = models.CharField(max_length=12, blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)
    fclass = models.CharField(max_length=28, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Waterbody'
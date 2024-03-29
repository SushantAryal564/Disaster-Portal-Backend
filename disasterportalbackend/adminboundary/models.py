from django.contrib.gis.db import models  

class Lalitpurmetro(models.Model):
    gid = models.AutoField(primary_key=True) 
    objectid = models.FloatField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True, srid=4326)
    palika = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LalitpurMetro'


class Ward(models.Model):
    gid = models.AutoField(primary_key=True) 
    ward = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True, srid=4326)
    number_of_disasters = models.IntegerField(blank=True, null=True)
    total_infrastructure_damaged = models.IntegerField(blank=True, null=True, default=0)
    total_estimated_loss = models.FloatField(blank=True, null=True, default=0)
    total_people_death = models.IntegerField(blank=True, null=True, default=0)
    centroid = models.GeometryField(srid=4326, blank=True, null=True)   
    class Meta:
        managed = False
        db_table = 'Ward'
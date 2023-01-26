from django.contrib.gis.db import models       


class Ward(models.Model):
    province = models.BigIntegerField()        
    district = models.CharField(max_length=50) 
    palika = models.CharField(max_length=50)   
    type = models.CharField(max_length=50)     
    ward = models.BigIntegerField()
    geom = models.PolygonField(srid=4326)
# Auto-generated `LayerMapping` dictionary for Spatialdata model
spatialdata_mapping = {
    'province': 'PROVINCE',
    'district': 'DISTRICT',
    'palika': 'PALIKA',
    'type': 'TYPE',
    'ward': 'WARD',
    'geom': 'POLYGON',
}

class LalitpurMetro(models.Model):
    objectid = models.BigIntegerField()        
    palika = models.CharField(max_length=50)   
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)  

# Auto-generated `LayerMapping` dictionary for LalitpurMetro model
lalitpurmetro_mapping = {
    'objectid': 'OBJECTID',
    'palika': 'PALIKA',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'POLYGON',
}
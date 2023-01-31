from django.db import models
from django.utils import timezone
from adminboundary.models import *
from django.db.models import Manager as GeoManager

class DisasterType(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    order = models.IntegerField()

class Rating(models.Model):
    order = models.IntegerField()

class ClusterType(models.Model):
    name = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)

class DisasterEvent(models.Model):
    name=models.CharField(max_length=100)
    Ward=models.ForeignKey(Ward,on_delete=models.PROTECT,blank=True,null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank = True, null=True)
    geom=models.GeometryField(blank=True,null=True)
    date_event= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed=models.DateTimeField(blank=True,null=True)
    registered_date= models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True , blank=True, null=True)
    is_verified = models.BooleanField(null=True, blank=True)
    is_closed = models.BooleanField(null=True,blank=True)
    type = models.ForeignKey(DisasterType,on_delete=models.PROTECT, blank=True, null=True )
    rating = models.ForeignKey(Rating,on_delete=models.PROTECT, null=True, blank=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startTime = models.DateTimeField(blank=True, null=True)
    expireTime = models.DateTimeField(blank=True, null=True)
    objects=GeoManager()
    
    def __str__(self):
        return str(super().__str__())+str(self.name)
    
    # def save(self,)


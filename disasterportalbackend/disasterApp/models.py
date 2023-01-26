from django.db import models
from django.utils import timezone
from adminboundary.models import *

class DisasterType(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    order = models.IntegerField(max=5, min=1)

class Rating(models.Model):
    order = models.IntegerField(max=5, min=1)

class ClusterType(models.Model):
    name = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)

class DisasterEvent(models.Model):
    name=models.CharField(max_length=100)
    Ward=models.ForeignKey(Ward,on_delete=models.PROTECT,blank=True,null=True)
    geom=models.GeometryField(blank=True,null=True)
    date_event= models.DateTimeField(blank=True,default=timezone.now,null=True)
    date_closed=models.DateTimeField(blank=True,null=True)
    is_closed=models.BooleanField(null=True,default=False)
    registered_date= models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(null=False, blank=False)
    is_closed = models.BooleanField(null=False,blank=False)
    type = models.ForeignKey(DisasterType,on_delete=models.PROTECT, blank=False, null=False )
    rating = models.ForeignKey(Rating, null=False, blank=False)
    source = models.CharField(max_length=100)
    description = models.TextField()
    startTime = models.DateTimeField()
    expireTime = models.DateTimeField()
    
    
    def __str__(self):
        return str(super().__str__())+str(self.name)


from django.db import models
from django.utils import timezone
from adminboundary.models import *
from django.db.models import Manager as GeoManager
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
class DisasterType(models.Model):
    title = models.CharField(max_length=100)
    icon = models.FileField(null=True, blank =True)
    type = models.CharField(max_length=100)
    order = models.IntegerField(blank = True, null =True);
    def __str__(self):
        return str(self.title)

class Rating(models.Model):
    order = models.IntegerField()
    def __str__(self):
        return str(self.order)

class ClusterType(models.Model):
    name = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)
    cluster_lead = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class DisasterEvent(models.Model):
    name=models.CharField(max_length=100)
    Ward=models.ForeignKey(Ward,on_delete=models.PROTECT,blank=True,null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank = True, null=True)
    geom=models.GeometryField(blank=True,null=True, srid=4326)
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
    peopleDeath = models.IntegerField(blank=True, null=True)
    estimatedLoss = models.IntegerField(blank=True, null=True)
    InfrastructureDestroyed = models.IntegerField(blank=True, null=True)
    peopleDeath = models.IntegerField(blank=True, null=True)
    objects=GeoManager()
    def save(self, *args, **kwargs):
        self.Ward.number_of_disasters += 1
        self.Ward.save()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(super().__str__())+str(self.name)

@receiver(post_delete, sender=DisasterEvent)
def decrement_ward_disasters(sender, instance, **kwargs):
    instance.Ward.number_of_disasters -= 1
    instance.Ward.save()

@receiver(post_save, sender=DisasterEvent)
def update_ward_disater_damge_loss(sender, instance, **kwargs):
    instance.Ward.total_infrastructure_damaged += instance.InfrastructureDestroyed
    instance.Ward.total_estimated_loss += instance.estimatedLoss
    instance.Ward.total_people_death += instance.peopleDeath
    instance.Ward.save()

@receiver(post_delete, sender=DisasterEvent)
def subtract_ward_disater_damge_loss(sender, instance, **kwargs):
    instance.Ward.total_infrastructure_damaged -= instance.InfrastructureDestroyed
    instance.Ward.total_estimated_loss -= instance.estimatedLoss
    instance.Ward.total_people_death -= instance.peopleDeath
    instance.Ward.save()
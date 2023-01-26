from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from disasterApp.models import *
from disasterApp.models import *
class ActivityLog(models.Model):
  action_name = models.CharField(max_length=255)
  deployed_inventory = models.IntegerField()
  time_of_action = models.DateTimeField(auto_now_add=True)
  disaster = models.ForeignKey(DisasterEvent, on_delete=models.CASCADE)
  def __str__(self):
        return self.action_name

@receiver(post_save, sender=DisasterEvent)
def create_activity_log(sender, instance, created, **kwargs):
  if created:
      ActivityLog.objects.create(
          action_name='disasterstart', 
          deployed_inventory=0, 
          time_of_action=timezone.now(), 
          disaster=instance
      )
class Volunters(models.Model):
  name=models.CharField(max_length=100)
  contact=models.CharField(max_length=100)
  availability=models.BooleanField(default=True)
  isdeployed=models.BooleanField(default=False)

class MunicipalPolice(models.Model):
  name=models.CharField(max_length=100)
    
#response Team for Ward iniciatives    
class WardResponseTeams(models.Model):
  name=models.CharField(max_length=100)
  disaster=models.ForeignKey(DisasterEvent,on_delete=models.CASCADE)
  deployed=models.BooleanField(default=False)

class WardResponseTeamMembers(models.Model):
  volunters=models.ForeignKey(Volunters,on_delete=models.CASCADE,blank=True,null=True)
  team=models.ForeignKey(WardResponseTeams,on_delete=models.CASCADE,blank=True,null=True)

class MuniResponseTeams(models.Model):
  name=models.CharField(max_length=100,blank=True,null=True)
  disaster=models.ForeignKey(DisasterEvent,on_delete=models.CASCADE)
  deployed=models.BooleanField(default=False)

class MuniResponseTeamMembers(models.Model):
  volunters=models.ForeignKey(Volunters,on_delete=models.CASCADE,blank=True,null=True)
  team=models.ForeignKey(WardResponseTeams,on_delete=models.CASCADE,blank=True,null=True)
  municipal_police= models.ForeignKey(MunicipalPolice,on_delete=models.CASCADE)

class InventoryCategory(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  createdOn = models.DateTimeField()
  updatedOn = models.DateTimeField()


class InventoryList(models.Model):
  category = models.ForeignKey(InventoryCategory,on_delete = models.PROTECT, blank=True, null=True)
  title = models.CharField(max_length=100)
  unit = models.CharField(max_length=100)

class InventoryWard(models.Model):
  item = models.ForeignKey(InventoryList,on_delete=models.PROTECT, blank=True, null=True)
  Ward = models.ForeignKey(Ward, on_delete=models.PROTECT, blank=True, null=True)
  modified_on = models.DateTimeField()
  quantity = models.IntegerField()

class InventoryMunicipality(models.Model):
  item = models.ForeignKey(InventoryList,on_delete=models.PROTECT, blank=True, null=True)
  quantity = models.IntegerField()
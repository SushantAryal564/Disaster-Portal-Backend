from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(DisasterType)
class DisasterAdmin(admin.ModelAdmin):
  list_display=['title']
admin.site.register(DisasterEvent)
admin.site.register(Rating)
admin.site.register(ClusterType)
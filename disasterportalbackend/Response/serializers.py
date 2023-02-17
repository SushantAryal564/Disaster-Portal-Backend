from rest_framework import  serializers
from .models import *
from disasterApp.serializers import *;

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'
        
class VoluntersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunters
        fields = '__all__'

class MunicipalPoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalPolice
        fields = '__all__'

class WardResponseTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardResponseTeams
        fields = '__all__'

class WardResponseTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardResponseTeamMembers
        fields = '__all__'

class MuniResponseTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuniResponseTeams
        fields = '__all__'

class MuniResponseTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuniResponseTeamMembers
        fields = '__all__'

class InventoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = '__all__'

class InventoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryList
        fields = '__all__'

class InventoryWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryWard
        fields = '__all__'

class InventoryMunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMunicipality
        fields = '__all__'
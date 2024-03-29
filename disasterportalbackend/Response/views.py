from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters import rest_framework as filters
from rest_framework  import filters as rest_filters
from .permission import *
from rest_framework_simplejwt.authentication import JWTAuthentication

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    # permission_classes = [ActivityLogPermission,]
    # authentication_classes = [JWTAuthentication]
    filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
    filterset_fields = {
    'disaster__is_closed':['exact'],
    'disaster__id':['exact'],
    'disaster__Ward':['exact'],
    }
    search_fields = ['disaster__is_closed', 'disaster__id']
    def perform_create(self, serializer):
        print(self.request.user)
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            serializer.save(logCreator=self.request.user)
        else:
            serializer.save();
    
class VoluntersViewSet(viewsets.ModelViewSet):
    queryset = Volunters.objects.all()
    permission_classes = [OnlyGet,]
    serializer_class = VoluntersSerializer

class MunicipalPoliceViewSet(viewsets.ModelViewSet):
    queryset = MunicipalPolice.objects.all()
    permission_classes = [OnlyGet,]
    serializer_class = MunicipalPoliceSerializer

class WardResponseTeamsViewSet(viewsets.ModelViewSet):
    queryset = WardResponseTeams.objects.all()
    permission_classes = [OnlyGet,]
    serializer_class = WardResponseTeamsSerializer

class WardResponseTeamMembersViewSet(viewsets.ModelViewSet):
    queryset = WardResponseTeamMembers.objects.all()
    serializer_class = WardResponseTeamMembersSerializer

class MuniResponseTeamsViewSet(viewsets.ModelViewSet):
    queryset = MuniResponseTeams.objects.all()
    serializer_class = MuniResponseTeamsSerializer

class MuniResponseTeamMembersViewSet(viewsets.ModelViewSet):
    queryset = MuniResponseTeamMembers.objects.all()
    serializer_class = MuniResponseTeamMembersSerializer

class InventoryCategoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryCategory.objects.all()
    serializer_class = InventoryCategorySerializer

class InventoryListViewSet(viewsets.ModelViewSet):
    queryset = InventoryList.objects.all()
    serializer_class = InventoryListSerializer

class InventoryWardViewSet(viewsets.ModelViewSet):
    queryset = InventoryWard.objects.all()
    serializer_class = InventoryWardSerializer

class InventoryMunicipalityViewSet(viewsets.ModelViewSet):
    queryset = InventoryMunicipality.objects.all()
    serializer_class = InventoryMunicipalitySerializer
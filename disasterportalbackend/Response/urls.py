from rest_framework import routers
from django.urls import path, include
from .views import *
router = routers.DefaultRouter()
router.register(r'activity', ActivityLogViewSet)
router.register(r'volunters', VoluntersViewSet)
router.register(r'police',MunicipalPoliceViewSet)
router.register(r'wardresponseteam',WardResponseTeamsViewSet)
router.register(r'wardresponseteammember',WardResponseTeamMembersViewSet)
router.register(r'muniresponseteams',MuniResponseTeamsViewSet)
router.register(r'muniresponseteammember',MuniResponseTeamMembersViewSet)
router.register(r'inventorycategory',InventoryCategoryViewSet)
router.register(r'inventorylist',InventoryListViewSet)
router.register(r'inventoryward',InventoryWardViewSet)
router.register(r'inventorymunicipality',InventoryMunicipalityViewSet)
urlpatterns = [
  path('', include(router.urls)),
]
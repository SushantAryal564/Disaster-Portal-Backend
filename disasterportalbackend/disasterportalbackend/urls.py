from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/response/',include("Response.urls")),
    path('api/v1/disaster/',include('disasterApp.urls')),
    path('api/v1/spatial/',include('adminboundary.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/',include("accounts.urls"))
]

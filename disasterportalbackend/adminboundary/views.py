from rest_framework import viewsets
from .models import *
from .serializer import *
from django_filters import rest_framework as filters
from rest_framework  import filters as rest_filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class LalitpurMetroViewSet(viewsets.ModelViewSet):
    queryset = Lalitpurmetro.objects.all()
    serializer_class = LalitpurMetroSerializer
class WardWithGeomViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    # filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
    # filterset_fields = {
    # 'ward_features_id':['exact'],
    # }
    # search_fields = ['gid','ward']
    
class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardWithoutGeomSerializer
    # filter_backends=[filters.DjangoFilterBackend,rest_filters.SearchFilter,rest_filters.OrderingFilter]
    # filterset_fields = {
    # 'gid':['exact'],
    # 'ward':['exaxt'],
    # }
    # search_fields = ['gid','ward']
class WardDetail(APIView):
    def get(self, request, ward_number):
        print("**********************")
        try:
            ward = Ward.objects.get(ward=ward_number)
            serializer = WardSerializer(ward)
            return Response(serializer.data)
        except Ward.DoesNotExist:
            return Response({'error': f'Ward with number {ward_number} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
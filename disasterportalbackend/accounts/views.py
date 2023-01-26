from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializer import *
class LoginAPI(APIView):
  def post(self, request):
    try:
      data= request.data
      print("******************")
      print(data);
      serializer = LoginSerializer(data = data)
      if serializer.is_valid():
        username = serializer.data['username']
        password = serializer.data['password']
        user = authenticate(username = username, password=password)
        if user is None:
          return Response({'message':'invalid password'})
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
      })
    except Exception as e:
      print(e)
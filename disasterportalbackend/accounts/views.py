from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializer import *
class LoginAPI(APIView):
  def post(self, request):
    try:
      data= request.data
      serializer = LoginSerializer(data = data)
      if serializer.is_valid():
        username = serializer.data['username']
        password = serializer.data['password']
        user = authenticate(username = username, password=password)
        if user is None:
          return Response({'message':'invalid password'})
        usertype = ""
        refresh = RefreshToken.for_user(user)
        if(user.ward):
          wardNumber = user.ward.ward
          usertype = "ward"
          return Response({
          'refresh': str(refresh),
          'user':usertype,
          'userId': user.ward.gid,
          'WardNumber':wardNumber,
          'access': str(refresh.access_token),
        })
        if(user.municipality):
          usertype = "munciplaity"
          return Response({
          'refresh': str(refresh),
          'user':usertype,
          'access': str(refresh.access_token),
        })

    except Exception as e:
      print(e)
      return Response({"message":"Internal Server Error"})
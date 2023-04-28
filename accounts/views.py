from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Customer,Vendor
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets

User = get_user_model()
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
     
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


#Class based view to update user
class UpdateUser(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def put(self, request):
      user = User.objects.get(id=request.user.id)
      serializer = UserSerializer(user, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordView(APIView):
    serializer_class = UpdatePasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def put(self, request):
        serializer = UpdatePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update(request.user, serializer.validated_data)
            return Response({'success': True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetails(viewsets.ModelViewSet):
  queryset = Vendor.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  serializer_class = VendorSerializer
  parser_classes = (MultiPartParser, FormParser)

  def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomerDetails(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  serializer_class = CustomerSerializer
  parser_classes = (MultiPartParser, FormParser)

  def perform_create(self, serializer):
        serializer.save(user=self.request.user)



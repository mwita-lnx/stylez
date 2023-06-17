from django.shortcuts import render

# Create your views here.

from .serializers import *
from .models import Customer,Vendor
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
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

class AccountActivation(APIView):
      def post(self, request):
        serializer = UserActivation(request.data)
        try:
            user = User.objects.get(email=serializer.data['email'])
        except(TypeError, ValueError, OverflowError, User.DoesNotExist,AttributeError):
            user = None
        if user is None:
                return Response({'status':'400','message':'Invalid Email'}, status=status.HTTP_400_BAD_REQUEST)
        elif not user.is_active :
            if serializer.data['mode'] == "GET_TOKEN":
                try:
                    token = short_genome = get_random_string(length=6, allowed_chars='ABCDEFGH1234567890')
                    user.verification_code = token
                    user.save()
                    send_mail(
                        subject='stylez email confirmation',
                        message= token,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[serializer.data['email']])
                    return Response({'status':'200','message':'Code successfully Sent'})
                except(TypeError, ValueError, OverflowError,AttributeError):
                    return Response({'status':'200','message':'code Failed To Send'})

            elif serializer.data['mode'] == "VERIFY_TOKEN":
                if  user.verification_code != serializer.data['token']:
                    return Response({'status':'400','message':'verification Failed : Kindly Resend '},status=status.HTTP_400_BAD_REQUEST)
                elif user.verification_code == serializer.data['token']:
                    user.is_active = True
                    user.verification_code = ''
                    user.save()
                    return Response({'status':'200','message':'Email successfully verified'})
        else:
            return Response({'status':'400','message':'Email is already active'},status=status.HTTP_400_BAD_REQUEST)



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

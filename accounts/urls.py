from django.urls import path
from .views import *



urlpatterns = [
  path("api/get-details",UserDetailAPI.as_view()),
  path('api/register',RegisterUserAPIView.as_view()),
  path('api/update-user',UpdateUsers.as_view()),
  path('api/update-password',UpdatePasswordView.as_view()),
]
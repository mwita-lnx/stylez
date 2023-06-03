from django.urls import path,include
from rest_framework import routers,renderers
from .views import *

router = routers.DefaultRouter()


vendor_list = VendorDetails.as_view({
    'get': 'list',
    'post': 'create'
})
vendor_detail = VendorDetails.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

customer_list = CustomerDetails.as_view({
    'get': 'list',
    'post': 'create'
})
customer_detail = CustomerDetails.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
  path("api/get-details",UserDetailAPI.as_view()),
  path('api/register',RegisterUserAPIView.as_view()),
  path('api/activate-account',AccountActivation.as_view()),
  path('api/update-user',UpdateUser.as_view()),
  path('api/update-password',UpdatePasswordView.as_view()),
  path('api/vendor/',vendor_list,),
  path('api/vendor-details/<int:pk>/', vendor_detail, name='vendor-detail'),
  path('api/customer/',customer_list,),
  path('api/customer-details/<int:pk>/', customer_detail, name='customer-detail'),
  path('api/',include(router.urls))
]

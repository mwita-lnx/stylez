from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('accounts.urls')),
  path('api-token-auth', views.obtain_auth_token)
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
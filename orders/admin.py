from django.contrib import admin

# Register your models here.

from django.apps import apps

order_models = apps.get_app_config('orders').get_models()

for model in order_models:
    admin.site.register(model)
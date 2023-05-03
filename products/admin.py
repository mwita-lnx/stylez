from django.contrib import admin

# Register your models here.

from django.apps import apps

product_models = apps.get_app_config('products').get_models()

for model in product_models:
    admin.site.register(model)
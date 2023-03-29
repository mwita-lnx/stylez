from django.contrib import admin

# Register your models here.

from django.apps import apps

accounts_models = apps.get_app_config('accounts').get_models()

for model in accounts_models:
    admin.site.register(model)

from django.contrib import admin
from . import models


@admin.register(models.Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']


@admin.register(models.RiskField)
class RiskFieldAdmin(admin.ModelAdmin):
    list_display = ['risk', 'label', 'required', 'active']


@admin.register(models.FieldOption)
class FieldOptionAdmin(admin.ModelAdmin):
    list_display = ['field', 'name']

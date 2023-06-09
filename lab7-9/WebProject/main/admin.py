from django.contrib import admin
from .models import *

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('width', 'length')

@admin.register(PrecipitationType)
class PTAdmin(admin.ModelAdmin):
    list_display = ('type',)

@admin.register(Precipitation)
class PrecipAdmin(admin.ModelAdmin):
    list_display = ('amount', 'type')

@admin.register(Position)
class PosAdmin(admin.ModelAdmin):
    list_display = ('longitude', 'latitude', 'area')

@admin.register(Total)
class TotalAdmin(admin.ModelAdmin):
    list_display = ('position', 'precipitation', 'date')

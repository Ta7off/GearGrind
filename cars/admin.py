from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'owner', 'is_listed']
    search_fields = ['make', 'model']
    list_filter = ['is_listed']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = ["username", "first_name", "last_name", "license_number"]
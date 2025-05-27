from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "tier")
    search_fields = ("name", "registration_number")
    list_filter = ("tier",)
    list_per_page = 20

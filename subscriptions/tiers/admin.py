from django.contrib import admin
from .models import Tier

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    list_filter = ("price",)
    list_per_page = 20

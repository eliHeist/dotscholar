from django.contrib import admin
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Tier

class TierAdminForm(forms.ModelForm):
    class Meta:
        model = Tier
        fields = "__all__"

    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=FilteredSelectMultiple("permissions", is_stacked=False),
        required=False,
    )

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    form = TierAdminForm
    list_display = ("name", "price")
    search_fields = ("name",)
    list_filter = ("price",)
    list_per_page = 20

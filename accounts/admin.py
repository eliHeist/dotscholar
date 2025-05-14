from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()
# Register your models here.
admin.site.site_header = 'MBF Auto Garage'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["Username", "email"]
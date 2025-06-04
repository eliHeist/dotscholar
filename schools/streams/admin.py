from django.contrib import admin
from .models import Stream

# Register your models here.
@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ["name", "current_class", "class_teacher"]
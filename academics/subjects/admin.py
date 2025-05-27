from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from .models import Subject, Paper, Category


class PaperInline(admin.TabularInline):
    model = Paper
    extra = 0  # Number of empty forms to display
    verbose_name = _("Paper")
    verbose_name_plural = _("Papers")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "abbreviation", "level", "category", "is_base", "school", "paper_count")
    list_filter = ("level", "category", "is_base", "school", "classes")
    search_fields = ("name", "code", "abbreviation")
    filter_horizontal = ("classes",)
    inlines = [PaperInline]
    fieldsets = (
        (_("General Information"), {"fields": ("name", "abbreviation", "code")}),
        (_("Details"), {"fields": ("level", "category", "is_base", "school", "classes")}),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(paper_count=Count("papers"))
        return queryset

    def paper_count(self, obj):
        return obj.paper_count

    paper_count.short_description = _("Number of Papers")


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ("get_name", "number", "subject")
    list_filter = ("subject",)
    search_fields = ("name", "number", "subject__name", "subject__code")

    def get_name(self, obj):
        return obj.get_name()

    get_name.short_description = _("Name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","subject_count")
    search_fields = ("name",)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(subject_count=Count("subjects"))
        return queryset
    
    def subject_count(self, obj):
        return obj.subject_count

    subject_count.short_description = _("Number of Subjects")
from django.urls import path

from . import views

app_name = "management"

urlpatterns = [
    path("", views.ManagementOverview.as_view(), name="overview"),
    path("terms/", views.ManagementTermsView.as_view(), name="terms"),
    path("classes/", views.ManagementClassesView.as_view(), name="classes"),
    path("subjects/", views.ManagementSubjectsView.as_view(), name="subjects"),
    path("subjects/setup/", views.SubjectsSetupView.as_view(), name="subjects_setup"),
]
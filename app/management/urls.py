from django.urls import path

from . import views

app_name = "management"

urlpatterns = [
    path("", views.ManagementOverview.as_view(), name="overview"),
]
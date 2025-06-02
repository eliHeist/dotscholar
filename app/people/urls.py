from django.urls import path

from . import views

app_name = "people"

urlpatterns = [
    path("", views.PeopleOverviewView.as_view(), name="overview"),
    path("users/", views.PeopleUserView.as_view(), name="users"),
]
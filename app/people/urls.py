from django.urls import path

from . import views

app_name = "people"

urlpatterns = [
    path("", views.PeopleOverviewView.as_view(), name="overview"),
    path("users/", views.PeopleUserView.as_view(), name="users"),
    path("students/", views.StudentsManagementView.as_view(), name="students"),
    path("students/new-enrollments/", views.StudentsNewEnrollmentsView.as_view(), name="new-students-enrollment"),
]
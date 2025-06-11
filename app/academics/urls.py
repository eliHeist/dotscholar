from django.urls import path
from . import views

app_name = "academics"

urlpatterns = [
    path('', views.ClassesAcademicsView.as_view(), name="classes"),
    path('<int:class_pk>/assessments/', views.ClassAssessmentsView.as_view(), name="assessments"),
]
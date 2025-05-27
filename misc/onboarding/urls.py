from django.urls import path

from . import views

app_name = "onboarding"

urlpatterns = [
    path("", views.OnboardingView.as_view(), name="onboard"),
]
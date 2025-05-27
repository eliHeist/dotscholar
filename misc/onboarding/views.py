from django.shortcuts import render
from django.views import View

# Create your views here.
class OnboardingView(View):
    template_name = "onboarding/onboarding.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
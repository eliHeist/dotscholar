from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LandingPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template_name = 'pages/landing.html'
        school = request.user.get_school()
        return render(request, template_name)

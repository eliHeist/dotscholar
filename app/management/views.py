from django.shortcuts import render
from django.views import View

# Create your views here.
class ManagementOverview(View):
    template_name = 'management/overview.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
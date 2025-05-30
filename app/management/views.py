from django.shortcuts import render
from django.views import View

from schools.terms.models import Term

# Create your views here.
class ManagementOverview(View):
    template_name = 'management/overview.html'

    def get(self, request, *args, **kwargs):
        # get active term for which this today is in 
        active_term = Term.objects.filter(active=True).first()
        context = {
            'active_term': active_term,
        }
        return render(request, self.template_name, context)
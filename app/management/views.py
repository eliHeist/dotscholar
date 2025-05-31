from django.shortcuts import render
from django.views import View

from schools.terms.models import Term

# Create your views here.
class ManagementOverview(View):
    template_name = 'management/overview.html'

    def get(self, request, *args, **kwargs):
        # get active term for which this today is in 
        current_term = Term.objects.filter(active=True).first()
        context = {
            'current_term': current_term,
        }
        return render(request, self.template_name, context)
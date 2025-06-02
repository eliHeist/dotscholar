from django.shortcuts import render
from django.views import View


class PeopleOverviewView(View):
    """
    View to render the overview page for people.
    """
    template_name = 'people/overview.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to render the overview page.
        """
        return render(request, self.template_name)

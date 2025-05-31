from django.shortcuts import render
from django.views import View

from academics.classes.models import Class
from schools.terms.models import Term

# Create your views here.
class ManagementOverview(View):
    template_name = 'management/overview.html'

    def get(self, request, *args, **kwargs):
        # get active term for which this today is in 
        user = request.user
        school = user.get_school()
        current_term = school.terms.filter(active=True).first()
        context = {
            'current_term': current_term,
        }
        return render(request, self.template_name, context)
    
class ManagementClassesView(View):
    template_name = 'management/classes.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()
        classes = Class.objects.all()
        streams = school.streams.all()

        # annotate each stream to a class
        for cls in classes:
            cls.streams = streams.filter(current_class=cls)

        context = {
            'classes': classes,
        }
        return render(request, self.template_name, context)
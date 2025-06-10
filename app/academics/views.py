from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class ClassesAcademicsView(LoginRequiredMixin, View):
    template_name = "academics/classes.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()
        classes = school.get_classes()
        
        context = {
            "classes": classes
        }
        return render(request, self.template_name, context)
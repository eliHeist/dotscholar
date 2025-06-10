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


class ClassSubjectsView(View):
    def get(self, request, class_pk, *args, **kwargs):
        school = request.user.get_school()
        class_ = school.get_classes().get(pk=class_pk)
        
        template_name = 'academics/class-subjects.html'
        context = {
            "class": class_,
        }
        return render(request, template_name, context)

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from academics.classes.models import Class
from people.teachers.models import Teacher

# Create your views here.
class ClassSubjectsView(View):
    def get(self, request, class_pk, *args, **kwargs):
        school = request.user.get_school()
        class_ = school.get_classes().get(pk=class_pk)
        
        template_name = 'academics/class-subjects.html'
        context = {
            "class": class_,
        }
        return render(request, template_name, context)


class ClassesAcademicsView(LoginRequiredMixin, View):
    template_name = "academics/classes.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()
        classes = school.get_bare_classes()
        
        teacher_object = Teacher.objects.get(pk=user.pk)
        
        assignments = teacher_object.teaching_assignments.all()

        streams = []
        for assignment in assignments:
            stream = assignment.stream
            streams.append(stream)
        
        for cls in classes:
            cls.stream_assignments = set() # to hold the streams that are matched
            for stream in streams:
                if stream.current_class == cls:
                    cls.stream_assignments.add(stream)
                
                # indicate if the stream belongs to the logged in user
                stream.mine = (stream.class_teacher == request.user)
        
        context = {
            "classes": classes
        }
        return render(request, self.template_name, context)




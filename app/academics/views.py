from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from academics.assessments.forms import AssessmentForm
from academics.assessments.models import Assessment
from academics.classes.models import Class
from people.teachers.models import Teacher

# Create your views here.
class ClassSubjectsView(LoginRequiredMixin, View):
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


class ClassAssessmentsView(LoginRequiredMixin, View):
    template_name = "academics/class-assessments.html"

    def redirect(self, class_pk):
        return redirect(reverse_lazy("academics:assessments", kwargs={"class_pk":class_pk}))
    
    def get(self, request, class_pk):
        school = request.user.get_school()
        cls = Class.objects.get(pk=class_pk)
        term = school.get_active_term()
        
        user = request.user
        teacher_object = Teacher.objects.get(pk=user.pk)
        assignments = teacher_object.teaching_assignments.all()
        
        all_papers = school.paper_group.papers.all()
        
        subjects = set()
        subject_ids = set()
        for assignment in assignments:
            subject = assignment.subject
            subject.school_papers = all_papers.filter(subject=subject)
            subjects.add(subject)
            subject_ids.add(subject.pk)
        
        
        assessments = Assessment.objects.filter(subject_id__in=subject_ids, term=term, cls=cls)
        
        form = AssessmentForm()
        
        context = {
            "subjects": subjects,
            "class": cls,
            "term": term,
            "assessments": assessments,
            "form": form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, class_pk):
        school = request.user.get_school()
        cls = Class.objects.get(pk=class_pk)
        term = school.get_active_term()
        
        print(request.POST)
        
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save()
            print(assessment)
            # assessment.term = term
            # assessment.cls = cls
            # assessment.save()
        else:
            print(form.errors)
            
        return self.redirect(class_pk)

from django.db import transaction
from django.shortcuts import render
from django.views import View

from academics.classes.models import Class
from academics.subjects.models import Paper, Subject
from people.teachers.models import Teacher
from schools.terms.models import Term


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


class ManagementTermsView(View):
    template_name = 'management/terms.html'

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

        for cls in classes:
            cls.school_streams = cls.get_streams(school)
        
        teachers = Teacher.objects.get_by_school(school)

        context = {
            'classes': classes,
            'teachers': teachers,
            'school': school,
        }
        return render(request, self.template_name, context)
    

class SubjectsSetupView(View):
    template_name = 'management/subjects_setup.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()
        
        with transaction.atomic():
            papers = school.paper_group.papers.all()
            all_base_subjects = Subject.objects.get_base().prefetch_related('papers')
        
        
        school_subjects = Subject.objects.from_papers(papers)
        
        levels = [
            {
                'code': 'O',
                'name': 'Ordinary',
                'subjects': school_subjects.filter(level='O')
            },
            {
                'code': 'A',
                'name': 'Advanced',
                'subjects': school_subjects.filter(level='A')
            }
        ]


        context = {
            'levels': levels,
            'all_base_subjects': all_base_subjects,
        }
        return render(request, self.template_name, context)
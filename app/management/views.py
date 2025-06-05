import json
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
import urllib

from academics.classes.models import Class
from academics.subjects.models import Paper, Subject
from people.teachers.models import Teacher
from schools.streams.models import Stream
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
    
    def post(self, request):
        data = request.POST
        user = request.user
        school = user.get_school()
        
        class_pk = data.get("class_pk")
        name = data.get("name")
        class_teacher = data.get("class_teacher")
        
        stream = Stream.objects.create(
            school=school,
            current_class=Class.objects.get(pk=int(class_pk)),
            name=name,
            class_teacher=Teacher.objects.get(pk=int(class_teacher)) if class_teacher else None
        )
        
        return redirect(reverse_lazy("management:classes"))
    
    def put(self, request, *args, **kwargs):
        decoded_body = request.body.decode("utf-8")
        parsed_data = urllib.parse.parse_qs(decoded_body)
        raw_stream = parsed_data.get("stream", [None])[0]
        
        user = request.user
        school = user.get_school()
        
        if raw_stream:
            stream_data = json.loads(raw_stream)

            # Now get the values
            stream_id = stream_data.get("id")
            name = stream_data.get("name")
            class_teacher = stream_data.get("class_teacher")

            print(name)
            
            stream = Stream.objects.get(pk=stream_id)
            stream.name=name
            stream.class_teacher=Teacher.objects.get(pk=int(class_teacher))
            stream.save()
            
            teachers = Teacher.objects.get_by_school(school)
            
            return render(request, 'management/fragments/stream-card.html', {"stream": stream, "teachers": teachers})
    

class ManagementSubjectsView(View):
    template_name = 'management/subjects.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()
        subjects = Subject.objects.get_for_school(school)
        levels = [
            {
                'code': 'O',
                'name': 'Ordinary',
                'subjects': subjects.filter(level='O')
            },
            {
                'code': 'A',
                'name': 'Advanced',
                'subjects': subjects.filter(level='A')
            }
        ]
        context = {
            'school': school,
            'levels': levels
        }
        return render(request, self.template_name, context)
    

class SubjectsSetupView(View):
    template_name = 'management/subjects_setup.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        school = user.get_school()

        context = {}
        return render(request, self.template_name, context)

from django.shortcuts import render
from django.views import View

from .models import Student

# Create your views here.
class StudentListView(View):
    def get(self, request):
        # Logic to retrieve and display a list of students
        students = Student.objects.all()
        context = {
            'students': students,
        }
        return render(request, 'students/student-list.html', context)



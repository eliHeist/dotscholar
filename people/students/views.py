from django.shortcuts import render

from .models import Student

# Create your views here.
class StudentListView:
    def get(self, request):
        # Logic to retrieve and display a list of students
        students = Student.objects.all()
        context = {
            'students': students,
        }
        return render(request, 'students/student-list.html', context)



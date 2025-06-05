from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class PeopleOverviewView(LoginRequiredMixin, View):
    """
    View to render the overview page for people.
    """
    template_name = 'people/overview.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to render the overview page.
        """
        return render(request, self.template_name)


class PeopleUserView(LoginRequiredMixin, View):
    """
    View to render the user profile page.
    """
    template_name = 'people/users.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to render the user profile page.
        """
        user = request.user
        school = user.get_school()
        users = User.objects.filter(school=school)
        context = {
            'users': users,
        }
        return render(request, self.template_name, context)


class StudentsManagementView(View):
    template_name = 'people/students.html'

    def get(self, request, *args, **kwargs):
        # get active term for which this today is in 
        user = request.user
        school = user.get_school()
        current_term = school.terms.filter(active=True).first()
        enrollments = current_term.enrollments.all()

        ids = [enrollment.student.pk for enrollment in enrollments]
        # get students whose id is not in ids
        non_enrolled_students = school.students.filter(active=True).exclude(pk__in=ids)

        context = {
            'current_term': current_term,
            'enrollments': enrollments,
            'non_enrolled_students': non_enrolled_students,
        }
        return render(request, self.template_name, context)

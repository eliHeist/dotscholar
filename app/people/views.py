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




from ninja import Router
from ninja.security import django_auth

from .schemas import TeacherSchema
from .models import Teacher

teacher_router = Router(auth=django_auth)


@teacher_router.get("", response=list[TeacherSchema])
def list_teachers(request):
    """
    List all teachers.
    """
    school = request.user.get_school()
    return Teacher.objects.get_by_school(school)

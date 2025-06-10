from ninja import Router
from ninja.security import django_auth

from .schemas import TeacherSchema, TeachingAssignmentInSchema
from .models import Teacher

teacher_router = Router(auth=django_auth)


@teacher_router.get("", response=list[TeacherSchema], url_name="teachers-list")
def list_teachers(request):
    """
    List all teachers.
    """
    school = request.user.get_school()
    return Teacher.objects.get_by_school(school)


# @teacher_router.get("", response=list[TeachingAssignmentInSchema], url_name="get_assignments")
# def get_assignments(request):
#     """
#     List all teachers.
#     """
#     school = request.user.get_school()
#     return Teacher.objects.get_by_school(school)

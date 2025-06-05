from django.db import transaction

from ninja import Router
from ninja.security import django_auth

from academics.classes.models import Class
from schools.enrollment.models import Enrollment

from .models import Student
from .schemas import NewStudentEnrollmentSchema, StudentSchema


students_router = Router(auth=django_auth)


@students_router.post('/new_student_enrollment', response=StudentSchema, url_name='new_student_enrollment')
def new_student_enrollment(request, payload: NewStudentEnrollmentSchema):
    user = request.user
    school = user.get_school()
    with transaction.atomic():
        student = Student.objects.create(
            first_name=payload.first_name,
            last_name=payload.last_name,
            middle_name=payload.middle_name,
            gender=payload.gender,
            payment_code=payload.payment_code,
            school=school
        )
        enrollment = Enrollment.objects.create(
            term=Class.objects.get(pk=payload.term),
            class_for=Class.objects.get(pk=payload.class_for),
            stream_for=Class.objects.get(pk=payload.stream_for),
            student=student
        )
    return student
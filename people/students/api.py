from typing import List
from django.db import transaction

from ninja import Router
from ninja.security import django_auth

from academics.classes.models import Class
from schools.enrollment.models import Enrollment
from schools.enrollment.schemas import EnrollmentDisplaySchema
from schools.streams.models import Stream
from schools.terms.models import Term

from .models import Student
from .schemas import NewStudentEnrollmentSchema, StudentSchema


students_router = Router(auth=django_auth)


@students_router.post('/new_student_enrollment', url_name='new_student_enrollment')
def new_student_enrollment(request, payload: List[NewStudentEnrollmentSchema]):
    user = request.user
    school = user.get_school()
    messages = []
    print(payload)
    with transaction.atomic():
        for student_data in payload:
            try:
                student_object = Student.objects.create(
                    first_name=student_data.first_name,
                    last_name=student_data.last_name,
                    middle_name=student_data.middle_name,
                    gender=student_data.gender,
                    payment_code=student_data.payment_code,
                    school=school
                )
                enrollment = Enrollment.objects.create(
                    term=Term.objects.get(pk=student_data.term),
                    class_for=Class.objects.get(pk=student_data.class_for),
                    stream_for=Stream.objects.get(pk=student_data.stream_for),
                    student=student_object
                )
                status = {
                    "error": False,
                    "message": "Success",
                }
            except Exception as e:
                status = {
                    "error": True,
                    "message": str(e),
                }
            messages.append(status)
            continue
            
    return messages
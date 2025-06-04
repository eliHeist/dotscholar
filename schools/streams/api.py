from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from academics.classes.models import Class
from people.teachers.models import Teacher

from .schemas import StreamSchema, StreamInSchema
from .models import Stream


streams_router = Router(auth=django_auth)

@streams_router.post("", response=StreamSchema, url_name="stream-create")
def create_stream(request, payload: StreamInSchema):
    print(payload)
    try:
        class_ = Class.objects.get(pk=payload.current_class)
        teacher = Teacher.objects.get(pk=payload.class_teacher)

        return Stream.objects.create(
            name=payload.name,
            current_class=class_,
            class_teacher=teacher,
            school=request.user.get_school(),
        )
    except Exception as e:
        raise HttpError(503, f"Failed to create stream: {e}") from e

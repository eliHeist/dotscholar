from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from .schemas import StreamSchema
from .models import Stream


streams_router = Router(auth=django_auth)

@streams_router.post("", response=StreamSchema, url_name="stream-create")
def create_stream(request, payload: StreamSchema):
    """
    Create a new stream.
    """
    try:
        return Stream.objects.create(
            name=payload.name,
            current_class=payload.current_class,
            school=request.user.get_school(),
        )
    except Exception as e:
        raise HttpError(503, f"Failed to create stream: {e}") from e

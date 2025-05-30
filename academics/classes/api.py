from typing import List

from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from .schemas import ClassSchema, Class

class_router = Router(auth=django_auth)


@class_router.get("", response=List[ClassSchema], url_name="class-list")
def classes_list(request):
    return Class.objects.all()
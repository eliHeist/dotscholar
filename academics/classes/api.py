from typing import List

from ninja import Router
from ninja.security import django_auth

from .schemas import ClassSchema, ClassFullSchema
from .models import Class

class_router = Router(auth=django_auth)


@class_router.get("", response=List[ClassSchema], url_name="class-list")
def classes_list(request):
    return Class.objects.all()


@class_router.get("school_classes/", response=List[ClassFullSchema], url_name="get_school_classes")
def get_school_classes(request):
    school = request.user.get_school()
    streams = school.streams.all()
    classes = Class.objects.all()

    for cls in classes:
        cls.school_streams = streams.filter(current_class=cls)
    
    return classes
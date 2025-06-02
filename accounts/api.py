from django.db import transaction

from ninja import Router
from ninja.security import django_auth

from .schemas import UserSchema, UserInSchema
from .models import User, UserProfile

user_router = Router(auth=django_auth)

@user_router.post("", response=UserSchema, url_name="user-add")
def create_user(request, data: UserInSchema):
    """
    Create a new user or teacher and their profile.
    """
    
    school = request.user.get_school()
    
    # create a random password for the user
    password = User.objects.make_random_password()
    
    with transaction.atomic():
        if getattr(data, "is_teacher", False):
            user = User.objects.create_teacher(
                email=data.email,
                first_name=data.first_name,
                last_name=data.last_name,
                password=password,
                school=school,
            )
        else:
            user = User.objects.create_user(
                email=data.email,
                first_name=data.first_name,
                last_name=data.last_name,
                password=password,
                school=school,
            )
        UserProfile.objects.create(
            user=user,
            gender=data.gender,
            phone_1=data.phone_1,
            phone_2=data.phone_2
        )
    return user
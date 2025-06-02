from ninja import ModelSchema, Schema

from .models import Teacher


class TeacherSchema(ModelSchema):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "email", "username", "is_active"]

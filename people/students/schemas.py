from ninja import ModelSchema

from .models import Student


class StudentSchema(ModelSchema):
    class Meta:
        model = Student
        model_fields = "__all__"

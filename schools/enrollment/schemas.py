from ninja import ModelSchema, Schema
from .models import Enrollment


class EnrollmentSchema(ModelSchema):
    class Meta:
        model = Enrollment
        fields = "__all__"
        

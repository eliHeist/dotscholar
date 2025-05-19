from ninja import ModelSchema

from .models import School


class SchoolSchema(ModelSchema):
    class Meta:
        model = School
        model_fields = "__all__"
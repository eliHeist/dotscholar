from ninja import ModelSchema

from .models import School


class SchoolSchema(ModelSchema):
    class Meta:
        model = School
        fields = "__all__"
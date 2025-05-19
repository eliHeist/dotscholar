from ninja import ModelSchema

from .models import Class


class ClassSchema(ModelSchema):
    class Meta:
        model = Class
        model_fields = "__all__"
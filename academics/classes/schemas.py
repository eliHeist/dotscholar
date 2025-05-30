from ninja import ModelSchema

from .models import Class


class ClassSchema(ModelSchema):
    class Meta:
        model = Class
        fields = "__all__"
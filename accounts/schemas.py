from ninja import ModelSchema

from .models import User


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = "__all__"
        # exclude = ["password"]
        model_exclude = ["password"]
from ninja import ModelSchema

from .models import Term


class TermSchema(ModelSchema):
    class Meta:
        model = Term
        model_fields = "__all__"
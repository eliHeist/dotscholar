from ninja import ModelSchema

from .models import Year


class YearSchema(ModelSchema):
    class Meta:
        model = Year
        model_fields = "__all__"

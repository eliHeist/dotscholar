from ninja import ModelSchema

from .models import Stream


class StreamSchema(ModelSchema):
    class Meta:
        model = Stream
        fields = "__all__"


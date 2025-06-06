from typing import List
from ninja import ModelSchema

from schools.streams.schemas import StreamSchema

from .models import Class


class ClassSchema(ModelSchema):
    class Meta:
        model = Class
        fields = "__all__"


class ClassFullSchema(ModelSchema):
    school_streams: List[StreamSchema] = None
    class Meta:
        model = Class
        fields = "__all__"
        
    @staticmethod
    def resolve_streams(obj:Class):
        return obj.school_streams


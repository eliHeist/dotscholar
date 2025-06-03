from ninja import ModelSchema, Schema

from .models import Stream


class StreamSchema(ModelSchema):
    enrollments_count:int = None
    class Meta:
        model = Stream
        fields = "__all__"
    
    
    @staticmethod
    def resolve_enrollments_count(obj:Stream):
        return obj.get_enrollments().count()


class StreamInSchema(Schema):
    name: str
    current_class: int
    class_teacher: int = None


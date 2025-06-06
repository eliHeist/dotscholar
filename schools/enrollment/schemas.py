from ninja import ModelSchema, Schema

from people.students.schemas import StudentSchema
from .models import Enrollment


class EnrollmentSchema(ModelSchema):
    class Meta:
        model = Enrollment
        fields = "__all__"


class EnrollmentDisplaySchema(ModelSchema):
    student: StudentSchema
    stream_name: str
    term_name: str
    class Meta:
        model = Enrollment
        fields = ["id", "student", "date_enrolled"]
    
    @staticmethod
    def resolve_stream_name(self):
        return self.stream_for.get_full_name()
    
    @staticmethod
    def resolve_term_name(self):
        return self.term.get_display_name
    

        

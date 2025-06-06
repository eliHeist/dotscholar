from ninja import ModelSchema, Schema

from .models import Student


class StudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = "__all__"



class NewStudentEnrollmentSchema(Schema):
    first_name:str
    last_name:str
    middle_name:str
    gender:str
    payment_code:str=None
    lin:str=None
    
    term:int
    class_for:int
    stream_for:int

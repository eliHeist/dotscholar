from typing import List
from ninja import ModelSchema, Schema

from .models import Teacher, TeachingAssignment


class TeacherSchema(ModelSchema):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "email", "username", "is_active"]


class TeachingAssignmentInSchema(Schema):
    id: int
    teacher: int
    subject: int
    papers: list[int] = None
    class_group: int
    streams: list[int] = None
    

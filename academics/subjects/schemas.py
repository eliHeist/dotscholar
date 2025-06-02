# academics/subjects/schemas.py
from ninja import ModelSchema, Schema
from .models import Subject, Paper


class SubjectSchema(ModelSchema):
    class Meta:
        model = Subject
        fields = ["id", "name", "abbreviation", "classes"]


class PaperSchema(ModelSchema):
    class Meta:
        model = Paper
        fields = "__all__"
        

class PaperRegistrationInSchema(Schema):
    level: str
    papers: list[int]


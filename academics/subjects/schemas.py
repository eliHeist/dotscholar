# academics/subjects/schemas.py
from ninja import ModelSchema
from .models import Subject, Paper


class SubjectSchema(ModelSchema):
    class Meta:
        model = Subject
        model_fields = ["id", "name", "abbreviation", "classes"]


class PaperSchema(ModelSchema):
    class Meta:
        model = Paper
        model_fields = ["id", "code", "title"]


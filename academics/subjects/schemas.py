# academics/subjects/schemas.py
from ninja import ModelSchema, Schema
from .models import SchoolPaperAssignment, Subject, Paper


class SubjectSchema(ModelSchema):
    class Meta:
        model = Subject
        fields = ["id", "name", "abbreviation", "classes"]


class PaperSchema(ModelSchema):
    class Meta:
        model = Paper
        fields = "__all__"

class PaperIdSchema(ModelSchema):
    class Meta:
        model = Paper
        fields = ["id"]

class SchoolPaperAssignmentSchema(ModelSchema):
    class Meta:
        model = SchoolPaperAssignment
        fields = ["paper", "is_compulsory"]
        

class PaperRegistrationInSchema(Schema):
    level: str
    papers: list[int]



class SchoolPaperAssignmentSchema(Schema):
    paper_id: int
    is_compulsory: bool

class CreateSchoolPapersGroupSchema(Schema):
    school_id: int
    paper_assignments: list[SchoolPaperAssignmentSchema]
    

class SubjectPapersSchema(ModelSchema):
    papers: list[PaperSchema] = []
    class Meta:
        model = Subject
        fields = ["id", "name", "code", "level", "classes", "is_base"]
    
    @staticmethod
    def resolve_papers(obj):
        return obj.papers.all()

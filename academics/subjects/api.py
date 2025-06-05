from typing import List

from django.db import transaction

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import django_auth

from .models import SchoolPapersGroup, Paper, SchoolPaperAssignment, Subject
from .schemas import PaperIdSchema, PaperSchema, PaperRegistrationInSchema, SchoolPaperAssignmentSchema, CreateSchoolPapersGroupSchema, SubjectPapersSchema

subjects_router = Router(auth=django_auth)


@subjects_router.put("/register_papers/", response=List[PaperSchema], url_name="register_papers")
def register_papers(request, payload: PaperRegistrationInSchema):
    user = request.user
    school = user.get_school()
    paper_group = school.paper_group
    
    with transaction.atomic():
        if not paper_group:
            paper_group = SchoolPapersGroup.objects.create(school=school)
        
        papers = Paper.objects.filter(id__in=payload.papers)
    
        paper_group.papers.add(*papers)
        paper_group.save()
    
    return papers


@subjects_router.post("/manage_school_papers/", url_name="manage_school_papers")
def create_school_papers_group(request, data: List[SchoolPaperAssignmentSchema]):
    school = request.user.get_school()
    school_paper_group = school.paper_group

    # Remove existing paper assignments that are not in the incoming data
    existing_paper_ids = [assignment.paper_id for assignment in data]

    school_paper_group.paper_assignments.exclude(paper_id__in=existing_paper_ids).delete()

    # Add or update paper assignments from the incoming data
    for assignment in data:
        paper = get_object_or_404(Paper, id=assignment.paper_id)
        school_paper_assignment, created = SchoolPaperAssignment.objects.get_or_create(
            school_papers_group=school_paper_group,
            paper=paper,
            defaults={'is_compulsory': assignment.is_compulsory}
        )
        if not created:
            school_paper_assignment.is_compulsory = assignment.is_compulsory
            school_paper_assignment.save()

    return {"message": "School papers group updated successfully"}

@subjects_router.get("school_papers/", response=List[SchoolPaperAssignmentSchema], url_name="get_school_papers")
def get_school_papers_group(request):
    school = request.user.get_school()
    return school.paper_group.paper_assignments.all()

@subjects_router.get("all_subjects/", response=List[SubjectPapersSchema], url_name="all_subjects")
def get_all_subjects(request):
    school = request.user.get_school()
    return Subject.objects.get_available_for_school(school).order_by('-name')


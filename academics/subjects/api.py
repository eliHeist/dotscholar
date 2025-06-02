from typing import List

from django.db import transaction

from ninja import Router
from ninja.security import django_auth

from .models import SchoolPapersGroup, Paper
from .schemas import PaperSchema, PaperRegistrationInSchema

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
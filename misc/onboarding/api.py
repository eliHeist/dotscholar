from django.db import transaction

from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from academics.subjects.models import Subject, SchoolPapersGroup
from accounts.models import User
from schools.schools.models import School
from subscriptions.tiers.models import Tier

from .schemas import CreateUserAndSchoolSchema

onboarding_router = Router()

@onboarding_router.post("/onboarding/", auth=django_auth, url_name="onboarding")
def onboarding(request, data: CreateUserAndSchoolSchema):
    """
    in an atomic transaction
    Create a school and assign to it the tier with order 0.
    then create a user, assign it to the school and set it as the owner.
    then create a SchoolPapersGroup, assign it to the school, get all subjects marked as default and add all their papers to the SchoolPapersGroup.
    save everything, if any error occurs, rollback the transaction. and return a good error message.
    """
    with transaction.atomic():
        try:
            # Create the school
            school = School.objects.create(
                name=data.school.name,
                short_name=data.school.short_name,
                tier=Tier.objects.get(order=0)  # Assuming a tier with order 0 exists
            )

            # Create the user and assign to the school
            user = User.objects.create_user(
                email=data.user.email,
                password=data.user.password,
                first_name=data.user.first_name,
                last_name=data.user.last_name,
                school=school,
                is_school_owner=True
            )

            # Create the SchoolPapersGroup and assign it to the school
            school_papers_group = SchoolPapersGroup.objects.create(
                school=school,
            )
            # Get all subjects marked as default and add their papers to the SchoolPapersGroup
            default_subjects = Subject.objects.filter(is_default=True, school=school)

            for subject in default_subjects:
                for paper in subject.papers.all():
                    school_papers_group.papers.add(paper)

            # Save the SchoolPapersGroup
            school_papers_group.save()

        except Exception as e:
            raise HttpError(503, f"{e}") from e
                    

    return {"message": "Onboarding successful"}
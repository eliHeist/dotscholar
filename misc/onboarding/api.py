from ninja import Router
from ninja.security import django_auth

from .schemas import CreateUserAndSchoolSchema

onboarding_router = Router()

@onboarding_router.post("/onboarding/", auth=django_auth, url_name="onboarding")
def onboarding(request, data: CreateUserAndSchoolSchema):
    """
    Handle onboarding requests.
    """
    return {"message": "Onboarding successful"}
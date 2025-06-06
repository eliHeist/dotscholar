from ninja import NinjaAPI

from academics.classes.api import class_router
from academics.subjects.api import subjects_router
from accounts.api import user_router
from misc.onboarding.api import onboarding_router
from schools.streams.api import streams_router
from schools.terms.api import terms_router
from people.teachers.api import teacher_router
from people.students.api import students_router


api_router = NinjaAPI(urls_namespace="api")

api_router.add_router("/onboarding/", onboarding_router)
api_router.add_router("/classes/", class_router)
api_router.add_router("/terms/", terms_router)
api_router.add_router("/streams/", streams_router)
api_router.add_router("/subjects/", subjects_router)
api_router.add_router("/accounts/", user_router)
api_router.add_router("/teachers/", teacher_router)
api_router.add_router("/students/", students_router)
from ninja import NinjaAPI

from academics.classes.api import class_router
from misc.onboarding.api import onboarding_router
from schools.terms.api import terms_router
from schools.streams.api import streams_router


api_router = NinjaAPI(urls_namespace="api")

api_router.add_router("/onboarding/", onboarding_router)
api_router.add_router("/classes/", class_router)
api_router.add_router("/terms/", terms_router)
api_router.add_router("/streams/", streams_router)
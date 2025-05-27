from ninja import NinjaAPI
from misc.onboarding.api import onboarding_router


api_router = NinjaAPI(urls_namespace="api")

api_router.add_router("/onboarding/", onboarding_router)
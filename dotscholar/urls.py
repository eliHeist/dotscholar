from django.contrib import admin
from django.urls import path, include

from api.api import api_router

from .appsConfig import getAppUrls

import django_unicorn

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("unicorn/", include("django_unicorn.urls")),
    path('api/', api_router.urls),
]

urlpatterns += getAppUrls()
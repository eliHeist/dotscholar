from django.urls import path, include

app_configs = [
	{ 'app_name': 'schools.streams', 'url': 'schools/streams/', 'namespace': 'streams' },

	{ 'app_name': 'schools.terms', 'url': 'schools/terms/', 'namespace': 'terms' },

	{ 'app_name': 'schools.periods', 'url': 'schools/periods/', 'namespace': 'periods' },

	{ 'app_name': 'schools.schools', 'url': 'schools/schools/', 'namespace': 'schools' },

	{ 'app_name': 'academics.classes', 'url': 'academics/classes/', 'namespace': 'classes' },

	{ 'app_name': 'people.parents', 'url': 'people/parents/', 'namespace': 'parents' },

	{ 'app_name': 'people.students', 'url': 'people/students/', 'namespace': 'students' },

	{ 'app_name': 'accounts', 'url': 'accounts/', 'namespace': 'accounts' },

	{ 'app_name': 'misc.staticpages', 'url': '', 'namespace': 'staticpages' },

	{ 'app_name': 'api', 'url': 'x_api/', 'namespace': 'x_api' },

    # { "app_name": "finances.payments", "url": "finances/payments", "namespace": "payments" },
]

def getAppUrls():
    urlpatterns = []
    for config in app_configs:
        urlpatterns.append(
            path(f"{config['url']}", include(f"{config['app_name']}.urls", namespace=config['namespace']))
        )
    return urlpatterns

def getAppNames():
    return [config['app_name'] for config in app_configs]

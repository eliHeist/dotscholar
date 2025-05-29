from django.urls import path, include

app_configs = [
	{ 'app_name': 'app.management', 'url': 'management/', 'namespace': 'management' },

	{ 'app_name': 'app.pages', 'url': 'app/pages/', 'namespace': 'pages' },

	{ 'app_name': 'misc.onboarding', 'url': 'misc/onboarding/', 'namespace': 'onboarding' },

	{ 'app_name': 'subscriptions.tiers', 'url': 'subscriptions/tiers/', 'namespace': 'tiers' },

	{ 'app_name': 'schools.enrollment', 'url': 'schools/enrollment/', 'namespace': 'enrollment' },

	{ 'app_name': 'people.staff', 'url': 'people/staff/', 'namespace': 'staff' },

	{ 'app_name': 'people.teachers', 'url': 'people/teachers/', 'namespace': 'teachers' },

	{ 'app_name': 'academics.subjects', 'url': 'academics/subjects/', 'namespace': 'subjects' },

	{ 'app_name': 'schools.streams', 'url': 'schools/streams/', 'namespace': 'streams' },

	{ 'app_name': 'schools.terms', 'url': 'schools/terms/', 'namespace': 'terms' },

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

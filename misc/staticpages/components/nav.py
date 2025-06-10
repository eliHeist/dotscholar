from django_unicorn.components import UnicornView
from django.utils.functional import SimpleLazyObject


class NavView(UnicornView):
    menu_items = [
        {
            "title": "Landing",
            "permissions": [],
            "links": [
                {
                    "title": "Home",
                    "icon": "icon-house",
                    "url": "pages:landing",
                    "permissions": [],
                },
            ],
        },
        {
            "title": "Management",
            "permissions": [],
            "links": [
                {
                    "title": "School",
                    "icon": "icon-house-plug",
                    "url": "management:overview",
                    "permissions": [],
                },
                {
                    "title": "People",
                    "icon": "icon-users-round",
                    "url": "people:overview",
                    "permissions": [],
                },
            ],
        },
        {
            "title": "Academics",
            "permissions": [],
            "links": [
                {
                    "title": "Classes",
                    "icon": "icon-house-plug",
                    "url": "academics:classes",
                    "permissions": [],
                },
            ],
        },
    ]

    permitted_menu = []

    def mount(self):
        arg = self.component_args[0]
        user = arg
        self.update_menu(user)

    def update_menu(self, user):
        """Filters the menu based on user permissions"""
        if not user:
            return
        if isinstance(user, SimpleLazyObject):
            user = user._wrapped

        permitted_menu = []

        for group in self.menu_items:
            permitted_links = []
            for link in group["links"]:
                # check if any has no permissions and add it
                if link["permissions"] == []:
                    permitted_links.append(link)
                # check if the user has the permissions listed
                elif any(user.has_perm(perm) for perm in link["permissions"]):
                    permitted_links.append(link)

            if permitted_links:
                permitted_menu.append(
                    {
                        "title": group["title"],
                        "links": permitted_links,
                    }
                )

        self.permitted_menu = permitted_menu

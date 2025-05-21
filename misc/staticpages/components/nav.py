from django_unicorn.components import UnicornView
from django.utils.functional import SimpleLazyObject


class NavView(UnicornView):
    menu_items = [
        {
            "title": "People",
            "icon": "icon-user-round",
            "permissions": ["students.view_student"],
            "links": [
                {
                    "title": "Students",
                    "url": "students:list",
                    "permissions": ["students.view_student"],
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
                        "icon": group["icon"],
                        "links": permitted_links,
                    }
                )

        self.permitted_menu = permitted_menu

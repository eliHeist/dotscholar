from django.contrib.auth.backends import BaseBackend

class TierPermissionBackend(BaseBackend):
    def has_perm(self, user_obj, perm, obj=None):
        """Checks if the user has a specific permission based on their school's tier.
        
        This method determines whether the given user possesses the requested permission by checking the permissions associated with their school's tier.

        Args:
            user_obj: The user object whose permissions are being checked.
            perm: The permission string in the format 'app_label.codename'.
            obj: Optional object instance for object-level permissions (unused).

        Returns:
            bool: True if the user has the specified permission, False otherwise.
        """
        if not user_obj.is_authenticated:
            return False

        # Parse permission into app_label and codename
        try:
            app_label, codename = perm.split(".")
        except ValueError:
            return False

        if school := getattr(user_obj, 'school', None):
            return (
                tier.permissions.filter(
                    content_type__app_label=app_label, codename=codename
                ).exists()
                if (tier := getattr(school, 'tier', None))
                else False
            )
        else:
            return False


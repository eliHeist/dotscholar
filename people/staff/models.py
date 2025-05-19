from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Staff(models.Model):

    first_name = models.CharField(_("First Name"), max_length=25)    
    middle_name = models.CharField(_("Middle Name"), max_length=25, null=True, blank=True)    
    last_name = models.CharField(_("Last Name"), max_length=25)
    gender = models.CharField(_("Gender"), max_length=5)

    class Meta:
        verbose_name = _("Staff")
        verbose_name_plural = _("Staffs")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

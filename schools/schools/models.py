from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    registration_number = models.CharField(_("Reg no."), max_length=50, unique=True)
    logo = models.FileField(_("Logo"), upload_to='school_logos', max_length=100, blank=True, null=True)
    tier = models.ForeignKey(
        "Tier",
        verbose_name=_("Tier"),
        on_delete=models.SET_NULL,
        related_name="schools",
    )

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name


    
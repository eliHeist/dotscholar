from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Subject(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbreviation = models.CharField(_("Abbreviation"), max_length=4)
    classes = models.ManyToManyField("academics.classes.Class", verbose_name=_("Classes"))

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Paper(models.Model):
    code = models.CharField(_("Paper Code"), max_length=10)
    title = models.CharField(_("Title"), max_length=20, null=True)

    class Meta:
        verbose_name = _("Paper")
        verbose_name_plural = _("Papers")

    def __str__(self):
        return self.name




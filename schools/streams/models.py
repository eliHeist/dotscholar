from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from schools.schools.models import School

# Create your models here.
class Stream(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.CASCADE)
    current_class = models.ForeignKey(Class, verbose_name=_("Class"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Stream")
        verbose_name_plural = _("Streams")

    def __str__(self):
        return self.name


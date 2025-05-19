from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Term(models.Model):
    number = models.DecimalField(_("Number"), max_digits=1, decimal_places=0)
    year = models.ForeignKey("schools.period.Year", verbose_name=_("Year"), on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")

    def __str__(self):
        return self.name


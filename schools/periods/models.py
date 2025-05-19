from django.db import models
from django.utils.translation import gettext_lazy as _

from schools.schools.models import School

# Create your models here.
class Year(models.Model):
    year = models.DecimalField(max_digits=4, decimal_places=0)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    
    class Meta:
        ordering = ["-year"]
        get_latest_by = "year"
        order_with_respect_to = 'school'
        verbose_name = "year"
        verbose_name_plural = "years"
        unique_together = ["year", "school"]

    def __str__(self):
        return self.name


class Day(models.Model):
    date = models.DateField()
    # term = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Day")
        verbose_name_plural = _("Days")

    def __str__(self):
        return self.name



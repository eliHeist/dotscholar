import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from schools.schools.models import School

# Create your models here.
current_year = datetime.date.today().year
min_year = 2010

today = datetime.date.today()
sept_1 = datetime.date(today.year, 9, 1)

years_add = 2 if today >= sept_1 else 1

YEAR_CHOICES = [(r, str(r)) for r in range(min_year, current_year + years_add)][::-1]

class Year(models.Model):
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=current_year,
        verbose_name=_("Year"),
        validators=[MinValueValidator(min_year), MaxValueValidator(current_year)]
    )
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    
    class Meta:
        ordering = ["-year"]
        get_latest_by = "year"
        # order_with_respect_to = 'school'
        verbose_name = "Academic Year"
        verbose_name_plural = "Academic Years"
        unique_together = ["year", "school"]

    def __str__(self):
        return self.name



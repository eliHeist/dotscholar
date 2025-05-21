from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from schools.periods.models import Year
from people.students.models import Student

# Create your models here.
class Term(models.Model):
    NUMBER_CHOICES = [
        (Decimal('1'), '1'),
        (Decimal('2'), '2'),
        (Decimal('3'), '3'),
    ]
    number = models.DecimalField(_("Number"), max_digits=1, decimal_places=0, choices=NUMBER_CHOICES)
    year = models.ForeignKey(Year, verbose_name=_("Year"), on_delete=models.DO_NOTHING)
    
    registered_students = models.ManyToManyField(Student, related_name=_("terms"))
    

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")
        unique_together = ("number", "year")
        ordering = ["year", "number"]

    def __str__(self):
        return f"{self.year} - {self.number}"


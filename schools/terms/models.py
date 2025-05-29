from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from people.students.models import Student

# Create your models here.
class Term(models.Model):
    NUMBER_CHOICES = [
        (Decimal('1'), '1'),
        (Decimal('2'), '2'),
        (Decimal('3'), '3'),
    ]
    number = models.DecimalField(_("Number"), max_digits=1, decimal_places=0, choices=NUMBER_CHOICES)
    start_date = models.DateField(_("Start Date"), unique=True)
    end_date = models.DateField(_("End Date"), unique=True)
    fees = models.PositiveIntegerField(_("Fees"), default=0)
    
    registered_students = models.ManyToManyField(Student, related_name=_("terms"))
    

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")
        unique_together = ("number", "start_date")
        ordering = ["start_date",]

    def __str__(self):
        return f"{self.year} - {self.number}"


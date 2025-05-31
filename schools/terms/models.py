from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from schools.schools.models import School

# Create your models here.
class Term(models.Model):
    NUMBER_CHOICES = [
        (Decimal('1'), '1'),
        (Decimal('2'), '2'),
        (Decimal('3'), '3'),
    ]
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="terms",
        verbose_name=_("School")
    )
    number = models.DecimalField(_("Number"), max_digits=1, decimal_places=0, choices=NUMBER_CHOICES)
    start_date = models.DateField(_("Start Date"), unique=True)
    end_date = models.DateField(_("End Date"), unique=True)
    active = models.BooleanField(_("Active"), default=True)
    

    class Meta:
        verbose_name = _("Term")
        verbose_name_plural = _("Terms")
        unique_together = ("number", "start_date")
        ordering = ["start_date",]

    def __str__(self):
        return f"{self.start_date} - {self.number}"
    
    def get_days(self):
        return (self.end_date - self.start_date).days
    
    def get_days_done(self):
        return (timezone.now().date() - self.start_date).days
    
    def get_day_number(self):
        return (timezone.now().date() - self.start_date).days + 1
    
    def get_days_left(self):
        return (self.end_date - timezone.now().date()).days


class TermFee(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name=_("fees"))
    classes = models.ManyToManyField(Class, related_name=_("term_fees"), blank=True)
    amount = models.PositiveIntegerField(_("Amount"), default=0)

    class Meta:
        verbose_name = _("Term Fee")
        verbose_name_plural = _("Term Fees")

    def __str__(self):
        return f"{self.classes} - {self.term} - {self.amount}"

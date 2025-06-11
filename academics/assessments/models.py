from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from academics.subjects.models import Paper, Subject
from schools.terms.models import Term


class KINDS(models.TextChoices):
    CONTINUOUS = "CA", _("Continuous Assessment")
    EXAM = "EX", _("Examination")

    
class Assessment(models.Model):

    kind = models.CharField(_("Kind"), max_length=5, choices=KINDS.choices, default=KINDS.CONTINUOUS)
    order = models.PositiveSmallIntegerField(default=0)
    term = models.ForeignKey(Term, verbose_name=_("Term"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE)
    cls = models.ForeignKey(Class, verbose_name=_("Class"), on_delete=models.CASCADE)

    date = models.DateField(_("Date"), null=True, blank=True)

    title = models.CharField(_("Title"), max_length=100)
    competency = models.TextField(_("Competency"), blank=True, null=True)
    papers = models.ManyToManyField(Paper, verbose_name=_("Papers"), blank=True)
    total_mark = models.PositiveSmallIntegerField(_("Total Mark"))

    class Meta:
        verbose_name = _("assessment")
        verbose_name_plural = _("assessments")
        unique_together = ("order", "term", "subject", "cls")

    def __str__(self):
        return self.title
    



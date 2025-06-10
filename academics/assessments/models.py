from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from academics.subjects.models import Paper, Subject
from schools.terms.models import Term


class Assessment(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    competency = models.TextField(_("Competency"), blank=True, null=True)
    term = models.ForeignKey(Term, verbose_name=_("Term"), on_delete=models.CASCADE)
    date = models.DateField(_("Date"), null=True, blank=True)
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE)
    papers = models.ManyToManyField(Paper, verbose_name=_("Papers"), blank=True)
    total_mark = models.PositiveSmallIntegerField(_("Total Mark"))

    class Meta:
        verbose_name = _("assessment")
        verbose_name_plural = _("assessments")

    def __str__(self):
        return self.title
    



from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.assessments.models import Assessment
from people.students.models import Student
from people.teachers.models import Teacher


class Mark(models.Model):

    assessment = models.ForeignKey(Assessment, verbose_name=_("Assessment"), on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(_("Score"))
    remarks = models.TextField(_("Remarks"), null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=_("Teacher"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Mark")
        verbose_name_plural = _("Marks")
        unique_together = ("assessment", "student")

    def __str__(self):
        return self.name



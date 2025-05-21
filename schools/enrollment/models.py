from django.db import models
from django.utils.translation import gettext_lazy as _

from people.students.models import Student
from schools.streams.models import Stream
from schools.terms.models import Term

# Create your models here.
class Enrollment(models.Model):
    term = models.ForeignKey(Term, verbose_name=_("Term"), on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, verbose_name=_("Stream"), on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    date_enrolled = models.DateField(_("Date Enrolled"), auto_now_add=True)

    class Meta:
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")

    def __str__(self):
        return self.student.get_full_name()

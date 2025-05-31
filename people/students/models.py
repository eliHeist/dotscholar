from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.subjects.models import Paper
from people.parents.models import Parent
from schools.schools.models import School
from schools.streams.models import Stream

# Create your models here.
class GenderOptions(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'

class Student(models.Model):
    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.CASCADE, related_name="students")
    date_added = models.DateField(_("Date added to system"), auto_now_add=True)

    first_name = models.CharField(_("First Name"), max_length=25)    
    middle_name = models.CharField(_("Middle Name"), max_length=25, null=True, blank=True)    
    last_name = models.CharField(_("Last Name"), max_length=25)
    gender = models.CharField(_("Gender"), max_length=1, choices=GenderOptions.choices)
    payment_code = models.CharField(_("Payment Code"), max_length=50)
    
    current_optional_papers = models.ManyToManyField(Paper, verbose_name=_("Optional Papers"), blank=True, related_name="current_students")

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
    
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class StudentParent(models.Model):

    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE, related_name="parent_relations")
    parent = models.ForeignKey(Parent, verbose_name=_("Parent"), on_delete=models.CASCADE, related_name="students_relations")
    title = models.CharField(
        max_length=50,
        choices=[
            ("father", _("Father")),
            ("mother", _("Mother")),
            ("guardian", _("Guardian")),
            ("brother", _("Brother")),
            ("sister", _("Sister")),
            ("uncle", _("Uncle")),
            ("aunt", _("Aunt")),
            ("grandfather", _("Grandfather")),
            ("grandmother", _("Grandmother")),
        ],
        default="mother",
    )

    class Meta:
        verbose_name = _("StudentParent")
        verbose_name_plural = _("StudentParents")
        unique_together = ("student", "parent")

    def __str__(self):
        return f"{self.title} of {self.student.get_full_name()} ({self.parent.full_name})"



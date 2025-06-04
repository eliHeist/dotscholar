from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from schools.schools.models import School
from people.teachers.models import Teacher

# Create your models here.
class Stream(models.Model):

    name = models.CharField(_("Name"), max_length=50, null=True, blank=True)
    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.CASCADE, related_name="streams")
    current_class = models.ForeignKey(Class, verbose_name=_("Class"), related_name="streams", on_delete=models.CASCADE)

    class_teacher = models.ForeignKey(
        Teacher, 
        verbose_name=_("Current Class Teacher"), 
        related_name="streams", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = _("Stream")
        verbose_name_plural = _("Streams")

    def __str__(self):
        return f"S.{self.current_class.number} {self.name}"
    
    def get_enrollments(self):
        return self.enrollments.filter(term__active=True)
    


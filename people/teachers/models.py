from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Teacher(models.Model):
    school = models.ForeignKey("schools.schools.School", verbose_name=_(""), on_delete=models.CASCADE)

    first_name = models.CharField(_("First Name"), max_length=25)    
    middle_name = models.CharField(_("Middle Name"), max_length=25)    
    last_name = models.CharField(_("Last Name"), max_length=25)
    gender = models.CharField(_("Gender"), max_length=5)
    
    papers = models.ManyToManyField("academics.subjects.Paper", verbose_name=_("Papers taught"))

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")

    def __str__(self):
        return self.name


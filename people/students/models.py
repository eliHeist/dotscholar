from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):
    school = models.ForeignKey("schools.schools.School", verbose_name=_(""), on_delete=models.CASCADE)
    date_added = models.DateField(_("Date added to system"), auto_now_add=True)

    first_name = models.CharField(_("First Name"), max_length=25)    
    middle_name = models.CharField(_("Middle Name"), max_length=25, null=True, blank=True)    
    last_name = models.CharField(_("Last Name"), max_length=25)
    gender = models.CharField(_("Gender"), max_length=5)
    payment_code = models.CharField(_("Payment Code"), max_length=50)
    
    current_optional_papers = models.ManyToManyField('academics.subjects.Paper', _("Optional Papers"), blank=True)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
    
    def get_full_name(self):
        return f""

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class, LevelChoices

# Create your models here.
class Subject(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbreviation = models.CharField(_("Abbreviation"), max_length=4, null=True, blank=True)
    code = models.CharField(_("Code"), max_length=3, unique=True)
    level = models.CharField(
        _("Level"),
        max_length=1,
        choices=LevelChoices.choices,
    )
    classes = models.ManyToManyField(Class, verbose_name=_("Classes"), related_name="subjects", blank=True)
    is_compulsory = models.BooleanField(_("Is Compulsory"), default=False)
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="subjects",
        null=True,
    )

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Paper(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE, related_name="papers")
    number = models.CharField(_("Number"), max_length=4)
    name = models.CharField(_("Name"), max_length=20, null=True)

    class Meta:
        verbose_name = _("Paper")
        verbose_name_plural = _("Papers")

    def __str__(self):
        return self.name
    
    def get_paper_code(self):
        return f"{self.subject.code}/{self.number}"


class Category(models.Model):

    name = models.CharField(_("Name"), max_length=20)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name





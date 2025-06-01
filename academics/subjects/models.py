from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class, LevelChoices
from schools.schools.models import School

# Create a subject manager with a method to get base subjects
class SubjectManager(models.Manager):
    def get_base(self):
        return self.filter(is_base=True)

    def get_default(self):
        return self.filter(is_default=True)
    

class Subject(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbreviation = models.CharField(_("Abbreviation"), max_length=4, null=True, blank=True)
    code = models.CharField(_("Code"), max_length=3, unique=True)
    level = models.CharField(
        _("Level"),
        max_length=1,
        choices=LevelChoices.choices,
        null=True,
        blank=True,
    )
    classes = models.ManyToManyField(Class, verbose_name=_("Classes"), related_name="subjects", blank=True)
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="subjects",
        null=True,
        blank=True,
    )
    is_base = models.BooleanField(_("Is Base"), default=False, help_text=_("Is this a base subject?"))
    is_default = models.BooleanField(_("Is Default"), default=False, help_text=_("Is this a default subject?"))
    school = models.ForeignKey(
        School,
        verbose_name=_("School"),
        on_delete=models.CASCADE,
        related_name="subjects",
        null=True,
        blank=True,
    )

    objects = SubjectManager()

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Paper(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE, related_name="papers")
    number = models.CharField(_("Number"), max_length=2)
    name = models.CharField(_("Name"), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _("Paper")
        verbose_name_plural = _("Papers")
        unique_together = (("subject", "number"),)

    def __str__(self):
        return self.get_name()
    
    def get_paper_code(self):
        return f"{self.subject.code}/{self.number}"
    
    def get_name(self):
        return self.name or f"{self.subject.name} Paper {self.number}"


class Category(models.Model):

    name = models.CharField(_("Name"), max_length=20, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class SchoolPapersGroup(models.Model):

    school = models.OneToOneField(School, verbose_name=_("School"), on_delete=models.CASCADE)
    papers = models.ManyToManyField(Paper, verbose_name=_("Papers"), related_name="school_papers_groups", blank=True)
    classes = models.ManyToManyField(Class, verbose_name=_("Classes"), related_name="paper_groups")

    class Meta:
        verbose_name = _("SchoolPapersGroup")
        verbose_name_plural = _("SchoolPapersGroups")

    def __str__(self):
        return self.name




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
    
    def from_papers(self, papers):
        """
        Returns a QuerySet of Subjects, each annotated with a 'matched_papers'
        attribute containing only the Paper objects from the provided papers
        (list or QuerySet) that belong to that Subject.

        Args:
            papers (list or QuerySet): A list or QuerySet of Paper objects.

        Returns:
            QuerySet: A QuerySet of Subject objects, with 'matched_papers' attribute.
        """
        if isinstance(papers, list):
            papers_queryset = Paper.objects.filter(pk__in=[paper.pk for paper in papers])
        elif isinstance(papers, models.QuerySet) and papers.model == self.model._meta.get_field('papers').related_model:
            papers_queryset = papers
        else:
            raise TypeError("papers must be a list or QuerySet of Paper objects.")

        paper_pks = papers_queryset.values_list('pk', flat=True)

        filtered_papers_prefetch = models.Prefetch(
            'papers',
            queryset=papers_queryset.filter(pk__in=paper_pks),
            to_attr='allowed_papers'
        )

        return (
            self.filter(papers__pk__in=paper_pks)
            .distinct()
            .prefetch_related(filtered_papers_prefetch)
        )
    
    def get_base(self):
        return self.filter(is_base=True)
    
    def get_available_for_school(self, school: School):
        base_subjects = self.get_base()
        school_subjects = self.filter(school=school)
        # return both sets in one queryset
        return base_subjects | school_subjects
    
    def get_for_school(self, school: School):
        school_papers = school.paper_group.papers.all()
        return self.from_papers(school_papers)
    
    def get_from_papers(self, papers):
        subjects = []
        for paper in papers:
            subject = paper.subject
            if subject not in subjects:
                subjects.append(subject)
        
        for subject in subjects:
            subject_papers = papers.filter(subject=subject)
            subject.papers_matched = subject_papers

        return subjects
    

class Subject(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbreviation = models.CharField(_("Abbreviation"), max_length=4, null=True, blank=True)
    code = models.CharField(_("Code"), max_length=4, unique=True)
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
    name = models.CharField(_("Name"), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("Paper")
        verbose_name_plural = _("Papers")
        unique_together = (("subject", "number"),)

    def __str__(self):
        return self.get_name()
    
    def get_paper_code(self):
        return f"{self.subject.code}/{self.number}"
    
    def get_name(self):
        return self.name or ""
    
    def get_full_name(self):
        return self.name or f"Paper {self.number}"


class Category(models.Model):

    name = models.CharField(_("Name"), max_length=20, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class SchoolPaperAssignment(models.Model):
    school_papers_group = models.ForeignKey('SchoolPapersGroup', on_delete=models.CASCADE, related_name='paper_assignments')
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE, related_name='school_assignments')
    is_compulsory = models.BooleanField(_('Is Compulsory'), default=False)

    class Meta:
        unique_together = (('school_papers_group', 'paper'),)
        verbose_name = _('School Paper Assignment')
        verbose_name_plural = _('School Paper Assignments')

    def __str__(self):
        return f"{self.paper} ({'Compulsory' if self.is_compulsory else 'Optional'}) - {self.get_level_display()}"

class SchoolPapersGroup(models.Model):
    school = models.OneToOneField(School, verbose_name=_("School"), on_delete=models.CASCADE, related_name="paper_group")
    papers = models.ManyToManyField(
        Paper,
        verbose_name=_("Papers"),
        related_name="school_papers_groups",
        blank=True,
        through='SchoolPaperAssignment',
        through_fields=('school_papers_group', 'paper'),
    )
    # classes = models.ManyToManyField(Class, verbose_name=_("Classes"), related_name="paper_groups")

    class Meta:
        verbose_name = _("SchoolPapersGroup")
        verbose_name_plural = _("SchoolPapersGroups")

    def __str__(self):
        return f"{self.school.name} Papers Group"




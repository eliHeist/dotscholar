from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from subscriptions.tiers.models import Tier


class School(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    short_name = models.CharField(_("Short Name"), max_length=10, blank=True, null=True)
    registration_number = models.CharField(_("Reg no."), max_length=50, unique=True, blank=True, null=True)
    logo = models.FileField(_("Logo"), upload_to='school_logos', max_length=100, blank=True, null=True)
    tier = models.ForeignKey(
        Tier,
        verbose_name=_("Tier"),
        on_delete=models.SET_NULL,
        related_name="schools",
        null=True,
    )

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name
    
    def get_subjects_group(self):
        """
        Returns the subject group for the school using the related name 'subject_group'.
        Returns None if it does not exist.
        """
        return getattr(self, 'paper_group', None)
    
    def get_teachers(self):
        """
        Returns all teachers associated with the school.
        """
        return self.users.filter(is_teacher=True)
    
    def get_active_term(self):
        """
        Returns the active term for the school.
        """
        return self.terms.filter(active=True).first()
        
    def get_classes(self):
        
        classes = Class.objects.all()
        for class_ in classes:
            class_.school_streams = class_.get_streams(self)
        return classes


    
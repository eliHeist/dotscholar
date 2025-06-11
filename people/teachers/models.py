from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from academics.classes.models import Class
from academics.subjects.models import Paper, Subject
from schools.schools.models import School
from schools.streams.models import Stream


User = get_user_model()


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_teacher=True)

    def create(self, **kwargs):
        kwargs.setdefault('is_teacher', True)
        return super().create(**kwargs)
    
    def get_by_school(self, school):
        """
        Returns all teachers associated with a specific school.
        """
        return self.filter(school=school, is_teacher=True)

class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def save(self, *args, **kwargs):
        # Ensure is_teacher is True when saving through the Teacher proxy
        self.is_teacher = True
        super().save(*args, **kwargs)
    
    # TODO: add the mechanism where a teacher is assigned to subjects that they teach only
    def get_subjects_taught(self):
        """
        Returns all subjects taught by the teacher.
        """
        return 0


class TeachingAssignment(models.Model):

    school = models.ForeignKey(School, verbose_name=_("School"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name=_("Subject"), on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, verbose_name=_("Teacher"), related_name="teaching_assignments")
    stream = models.ForeignKey(Stream, verbose_name=_("Streams"), on_delete=models.CASCADE, blank=True, related_name="teaching_assignments")
    
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class Meta:
        verbose_name = _("teaching assignment")
        verbose_name_plural = _("teaching assignments")
        unique_together = ("subject", "school", "stream")

    def __str__(self):
        return f"{self.school} - {self.subject} - {self.stream}"



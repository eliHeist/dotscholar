from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# Create your models here.
class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_teacher=True)

    def create(self, **kwargs):
        kwargs.setdefault('is_teacher', True)
        return super().create(**kwargs)

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


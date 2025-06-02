from django.db import models
from django.utils.translation import gettext_lazy as _


class LevelChoices(models.TextChoices):
    # PRIMARY = "P", _("Primary")
    ORDINARY = "O", _("Ordinary")
    ADVANCED = "A", _("Advanced")

class Class(models.Model):
    level = models.CharField(max_length=1, choices=LevelChoices.choices)
    number = models.CharField(max_length=1, choices=[(str(i), str(i)) for i in range(1, 8)], unique=True)

    def __str__(self):
        return f"S.{self.number}"
    
    def get_name(self):
        return f"S.{self.number}"
    
    def get_streams(self, school):
        return self.streams.filter(school=school)


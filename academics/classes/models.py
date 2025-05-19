from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 7)], unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


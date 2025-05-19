from django.db import models

# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
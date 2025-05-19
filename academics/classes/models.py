from django.db import models

# Create your models here.
class Class(models.Model):
    number = models.DecimalField(choices=[(i, str(i)) for i in range(1, 7)], unique=True, max_digits=1, decimal_places=0)

    def __str__(self):
        return f"S.{self.number}"


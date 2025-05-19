from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    registration_number = models.CharField(_("Reg"), max_length=50, unique=True)
    logo = models.FileField(_("Logo"), upload_to='school_logos', max_length=100)
    
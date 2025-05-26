from django.db import models
from django.utils.translation import gettext_lazy as _


class Parent(models.Model):

    full_name = models.CharField(max_length=25, verbose_name="Full Name")
    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=15)
    phone_2 = models.CharField(_("Phone 2"), max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    
    
    class Meta:
        verbose_name = _("parent")
        verbose_name_plural = _("parents")

    def __str__(self):
        return self.full_name


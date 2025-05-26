from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Tier(models.Model):

    name = models.CharField(_("Name"), max_length=50, unique=True)
    order = models.PositiveSmallIntegerField(_("Order"), help_text=_("Order of the tier in the list"), unique=True, null=True, blank=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=0, help_text=_("Price of the tier"))

    permissions = models.ManyToManyField('auth.Permission', verbose_name=_("Permissions"), blank=True)

    class Meta:
        verbose_name = _("Tier")
        verbose_name_plural = _("Tiers")
        ordering = ['order']

    def __str__(self):
        return self.name

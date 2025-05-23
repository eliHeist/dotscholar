from django.db import models


class Parent(models.Model):

    full_name = models.CharField(max_length=25, verbose_name="Full Name")
    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True)
    phone = models.PhoneNumberField(_("Phone"), max_length=15)
    phone_2 models.PhoneNumberField(_("Phone 2"), max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    students = models.ManyToManyField(Student, verbose_name=_("Students"))
    
    relation_role = models.CharField(
        max_length=50,
        choices=[
            ("father", _("Father")),
            ("mother", _("Mother")),
            ("guardian", _("Guardian")),
            ("brother", _("Brother")),
            ("sister", _("Sister")),
            ("uncle", _("Uncle")),
            ("aunt", _("Aunt")),
            ("grandfather", _("Grandfather")),
            ("grandmother", _("Grandmother")),
            ("other", _("Other")),
        ],
        default="mother",
    )
    

    class Meta:
        verbose_name = _("parent")
        verbose_name_plural = _("parents")

    def __str__(self):
        return self.full_name


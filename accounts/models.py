from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Group,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission

from schools.schools.models import School


# Create your models here.
class UserManager(BaseUserManager):
    """Class to manage the creation of user objects"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a user object
        Arguments:
        email: the string to use as email
        password: the string to use as password

        Optionals:
        Any additional fields to set on the User model

        Return:
            A user object
        """

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates an admin user object
        Arguments:
        username: the string to use as username
        email: the string to use as email
        password: the string to use as password

        Return:
            A user object
        """
        user = self.create_user(email, password=password)
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    username = models.CharField(max_length=25, unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school = models.ForeignKey(
        School, 
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )
    is_school_owner = models.BooleanField(default=False, verbose_name=_("Is School Owner"))

    is_teacher = models.BooleanField(default=False, verbose_name=_("Is Teacher"))

    profile = models.OneToOneField("UserProfile", verbose_name=_("Profile"), on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username or self.email

    def delete(self, using=None, keep_parents=False):
        self.is_active ^= True
        self.save()

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_school(self):
        """Returns the school of the user"""
        return self.school

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin



class UserProfile(models.Model):
    class Genders(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
    
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=Genders.choices, default=Genders.MALE)
    phone_1 = models.CharField(_("Phone (Main)"), max_length=20)
    phone_2 = models.CharField(_("Phone (Other)"), max_length=20, null=True, blank=True)
    
    
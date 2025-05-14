from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model, forms as auth_forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template import loader
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.html import strip_tags



class PasswordResetForm(auth_forms.PasswordResetForm):
    pass


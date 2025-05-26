from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from academics.classes.base_setup import setup_classes

User = get_user_model()

class Command(BaseCommand):
    help = 'Setup Base'

    def handle(self, *args, **kwargs):
        
        setup_classes()



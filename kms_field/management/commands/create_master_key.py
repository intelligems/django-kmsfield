import datetime

from django.core.management.base import BaseCommand
from kms_field.helpers import generate_cmk


class Command(BaseCommand):
    help = 'Create a new CMK - Customer Master Key.'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--description', type=str, help='Define a description for CMK',)

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        description = options.get('description') or f'KMSField CMK {now.strftime("%d-%m-%y %H:%M")}'

        cmk = generate_cmk(description)
        self.stdout.write(cmk)

from django.core.management.base import BaseCommand
from kms_field.helpers import generate_cmk


class Command(BaseCommand):
    help = 'Create a new CMK - Customer Master Key.'

    def add_arguments(self, parser):
        parser.add_argument('-d', '--description', type=str, help='Define a description for CMK',)

    def handle(self, *args, **options):
        description = options.get('description')

        cmk = generate_cmk(description)
        self.stdout.write(msg=cmk)


from django.core.management.base import BaseCommand, CommandError
from shelf.models import *

class Command(BaseCommand):
    help = "the help variable is there"
    requires_migrations_checks = True
    # arguments addition and validations
    def add_arguments(self, parser):
        parser.add_argument('author_id', nargs='+', type=int)

    # the real code that runs
    def handle(self, *args, **options):
        for author in Author.objects.all():
            print(author.first_name)

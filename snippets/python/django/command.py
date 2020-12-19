from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = '???'

    def add_arguments(self, parser):
        parser.add_argument('arg', nargs='+', type=int)

    def handle(self, *args, **options):
        options['arg']
        raise CommandError('%s' % 'data')

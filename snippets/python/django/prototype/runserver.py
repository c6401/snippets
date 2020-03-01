from django.core.management import call_command

call_command('migrate')
call_command('runserver', '8080', '--noreload')

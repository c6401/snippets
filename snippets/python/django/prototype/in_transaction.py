from django.db import transaction

with transaction.atomic():

    raise

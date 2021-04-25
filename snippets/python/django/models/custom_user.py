# AUTH_USER_MODEL = 'myapp.User'

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(
    DEBUG=True,
    SECRET_KEY="secret-key",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.staticfiles",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
        }
    ],
    STATIC_URL="/static/",
)

def index(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path("", index),
]

if __name__ == "__main__":
    execute_from_command_line()

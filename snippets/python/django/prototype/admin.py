from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.urls import path


class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
]

call_command('migrate')
User = get_user_model()
User.objects.create_superuser(username='admin', email='', password='admin')

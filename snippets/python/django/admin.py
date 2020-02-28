from django.contrib import admin
from myproject.myapp.models import ...

class ...Admin(admin.ModelAdmin):
    pass

admin.site.register(..., ...Admin)

from django.contrib import admin

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)


from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

class MyInline(TabularInline):
    model = MyModel


class MyAdmin(admin.ModelAdmin):
    inlines = [
        MyInline,
    ]

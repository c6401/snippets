MyModel.objects.values(
    '???'
).annotate(
    count=Count('id')
)

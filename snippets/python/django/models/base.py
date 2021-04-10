class MyModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = [
            ('???', '???'),
        ]
        verbose_name = 'My model'
        verbose_name_plural = 'My models'

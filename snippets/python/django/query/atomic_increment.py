model.counter = models.F('counter') + 1
model.save(update_fields=['counter'])
# model.refresh_from_db()

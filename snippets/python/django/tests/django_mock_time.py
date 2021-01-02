now = datetime(2030, 1, 1)
with patch('django.utils.timezone.now', Mock(return_value=now)):

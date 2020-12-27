from django.test.client import RequestFactory

factory = RequestFactory()
get_request = factory.get('/ping/')
post_request = factory.post('/item/', {'key': 'value'})

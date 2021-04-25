from django.middleware.csrf import get_token
from django.http import JsonResponse
url(r'^csrf', lambda r: JsonResponse({'csrf': get_token(r)})),

import httpx
import httpretty

httpretty.enable()

httpretty.register_uri(
    httpretty.GET, 'http://example.com/',
    body='Hello, World!',
    status=200
)

client = httpx.Client()
response = client.get('http://example.com/')

print(response.text)

httpretty.disable()
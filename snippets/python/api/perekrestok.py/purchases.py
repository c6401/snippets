import httpx
import browsercookie
from urllib.parse import unquote

_COOKIES = browsercookie.firefox()  # chrome?

token = unquote(next(c for c in _COOKIES if 'perekrestok.accessToken' in c.name).value)

async with httpx.AsyncClient() as client:
    response = await client.get(
        'https://my.perekrestok.ru/api/v4/transactions/list?limit=50',
        headers={"X-Authorization": token},
    )
    ids = ','.join(i['id'] for i in response.json()['data'] if i['type'] == 'buy')
    response = await client.get(
        f'https://my.perekrestok.ru/api/v4/transactions/details?id={ids}',
        headers={"X-Authorization": token},
    )
response.json()

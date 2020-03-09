import httpx
import browsercookie

_COOKIES = browsercookie.firefox()  # chrome?

async with httpx.AsyncClient() as client:
    response = await client.get('https://...', cookies=_COOKIES)

response.text

import httpx
import browsercookie

cookies = browsercookie.firefox()  # chrome?

async with httpx.AsyncClient() as client:
    response = await client.get('https://...', cookies=cookies)

response.text

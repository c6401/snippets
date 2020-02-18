import httpx

async with httpx.AsyncClient() as client:
    response = await client.get('https:...')

import httpx


async def stream(method, url, **kwargs):
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(method, url, **kwargs) as resp:
            async for chunk in resp.aiter_bytes():
                yield chunk

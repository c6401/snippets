import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com') as response:
        print(response.status)
        print(await response.text())
        # print(await response.json())

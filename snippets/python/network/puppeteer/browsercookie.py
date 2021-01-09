import asyncio
from urllib.parse import urlparse

from browsercookie import firefox as get_jar
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def func():
    url = 'https://...'
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await stealth(page)
    await page.setCookie(*[
        dict(name=c.name, value=c.value, domain=c.domain)
        for c in get_jar() if urlparse(url).hostname in c.domain
    ])
    await page.goto(url)

    # element = (await page.xpath('//...'))[0]

    await browser.close()

asyncio.get_event_loop().run_until_complete(func())

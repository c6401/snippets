import asyncio
from pyppeteer import launch
from browsercookie import firefox as get_jar

async def func():
    browser = await launch()
    page = await browser.newPage()
    await page.setCookie(*[dict(name=c.name, value=c.value, domain=c.domain) for c in get_jar() if domain in c.domain])
    await page.goto(address)
    await browser.close()

asyncio.get_event_loop().run_until_complete(func())

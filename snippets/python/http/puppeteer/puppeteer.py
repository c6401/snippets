import asyncio

from pyppeteer import launch

async def func():
    browser = await launch()
    page = await browser.newPage({'headless': False})
    await page.goto('...')

    await browser.close()

asyncio.get_event_loop().run_until_complete(func())

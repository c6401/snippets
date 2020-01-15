import asyncio
from urllib.parse import urlparse

from browsercookie import firefox as cookies
from pyppeteer import launch

url = 'https://'
browser = await launch({'headless': False})
page = await browser.newPage()
await page.setCookie(*[
    dict(name=c.name, value=c.value, domain=c.domain)
    for c in cookies() if urlparse(url).hostname in c.domain
])
await page.goto(url)

await browser.close()

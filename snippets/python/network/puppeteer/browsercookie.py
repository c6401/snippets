from urllib.parse import urlparse

from browsercookie import firefox
from pyppeteer import launch
# from pyppeteer_stealth import stealth

cookies = firefox(cookie_file=[''])

url = 'https://...'
browser = await launch({'headless': False})
page = await browser.newPage()
# await stealth(page)
await page.setCookie(*[
    dict(name=c.name, value=c.value, domain=c.domain)
    for c in cookies if urlparse(url).hostname in c.domain
])
await page.goto(url)

# element = (await page.xpath('//...'))[0]

await browser.close()

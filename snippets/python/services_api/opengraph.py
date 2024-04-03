tree = html.fromstring(response.content)  # type: lxml.html
url = tree.xpath('//meta[@property="og:url"]/@content')[0]
title_el = tree.xpath('//meta[@property="og:title"]/@content')[0]
description_el = tree.xpath('//meta[@property="og:description"]/@content')[0]

from aiohttp import web

app = web.Application()
routes = web.RouteTableDef()

@routes.get('/{path}')
async def get_url(request):
    path = request.match_info.get('path')

    return web.json_response({
        'path': path,
        'query': list(request.query.items()),
    }, status=200)
    # return web.Response(text='ok')

@routes.post('/{path}')
async def post_url(request):
    path = request.match_info.get('path')

    return web.json_response({
        'path': path,
        'query': list(request.query.items()),
        'text': await request.text(),
        # 'json': await request.json(),
        # 'form': list((await request.post()).items()),
        # 'multipart': list((await request.multipart()).items()),
    }, status=201)

app = web.Application()
app.add_routes(routes)

web.run_app(app)

# runner = web.AppRunner(app)
# await runner.setup()
# site = web.TCPSite(runner)
# await site.start()

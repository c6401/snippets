import json
from aiohttp import web
app = web.Application()
routes = web.RouteTableDef()

@routes.get('/init')
async def init_handler(r):
    return web.Response(text='''
        function getProxy(expr='') {
          return new Proxy(function() {}, {
            get(obj, path) {
              if (path !== 'then') {
                  return getProxy(expr ? `${expr}.${path}`: path);
              }
              async function request() {
                return await(await fetch('http://localhost:8080/eval', {
                  method: 'POST', body: expr,
                })).json();
              }
              let promise = request();
              return promise.then.bind(promise);
            },
            apply(target, thisArg, args) {
              var kwargs = {};
              if (Object.prototype.toString.call(args[args.length - 1]) === '[object Object]') {
                var kwargs = args.pop();
              }
              expr = `${expr}(*${JSON.stringify(args)}, **${JSON.stringify(kwargs)})`;
              return getProxy(expr);
            },
          });
        }
        window.py = getProxy()
    ''')

@routes.post('/eval')
async def eval_handler(r):
    code = await r.text()
    result = json.dumps(eval(code, globals()))
    return web.Response(text=result)

app.add_routes(routes)
runner = web.AppRunner(app)
await runner.setup()
site = web.TCPSite(runner)
await site.start()

# %%html
# <script src="http://localhost:8080/init"></script>

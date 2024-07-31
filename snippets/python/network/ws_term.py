
#pip install websockets
import asyncio as a
import websockets

loop = a.get_event_loop()

async def rx(ws):
    async for message in ws:
        print(f"\n< {message}", end='', flush=True)

async def tx(ws):
    while True:
        message = await loop.run_in_executor(None, lambda: input('> '))
        await ws.send(message)

async def term(ws, path):
    print(f"{ws.remote_address}")
    await a.gather(a.ensure_future(rx(ws)), a.ensure_future(tx(ws)))

loop.run_until_complete(websockets.serve(term, 'localhost', 8080))
loop.run_forever()

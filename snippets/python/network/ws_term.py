
#pip install websockets
import asyncio
import websockets

async def consumer(ws):
    async for message in ws:
        print(message)

async def producer(ws):
    while True:
        message = await asyncio.to_thread(input)
        await ws.send(message)

async def handler(ws):
    await asyncio.gather(consumer(ws), producer(ws))

async def main():
    async with websockets.serve(handler, 'localhost', 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())
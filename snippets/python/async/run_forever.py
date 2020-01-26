import asyncio

loop = asyncio.get_event_loop()
loop.create_task(...())
loop.run_forever()
loop.close()

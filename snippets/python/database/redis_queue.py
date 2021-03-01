import asyncio
import aioredis

redis = await aioredis.create_redis('redis://localhost:6379/0', encoding='utf-8')

await redis.rpush('myqueue', 'mymessage')

await redis.blpop('myqueue')

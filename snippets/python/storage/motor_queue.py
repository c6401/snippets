import asyncio
import logging
from pymongo.cursor import CursorType

# create mongo

collection = await mongo.bd.create_collection('...', capped=True, size=1000000)

async def queue(db, consumer: str, topic: str, query={}, interval=5 * 60):
    offsets = db.offsets
    offset = await offsets.find_one({'consumer': consumer, 'topic': topic})
    query = query.copy()
    if offset:
        query.update({'_id': {'$gt': offset['offset']}})

    collection = db[topic]
    cursor = collection.find(query, cursor_type=CursorType.TAILABLE)

    while True:
        async for result in cursor:
            yield result
            await offsets.update_one(
                {'consumer': consumer, 'topic': topic},
                {'$set': {'offset': result['_id']}},
                True,
            )
        logging.info(f'{consumer} to {topic} sub is going to sleep')
        await asyncio.sleep(interval)

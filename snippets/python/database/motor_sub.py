import asyncio
import logging
# create mongo

async def sub(consumer: str, topic: str, query={}, interval=5 * 60):
    offset = mongo.common.offset
    last = await offset.find_one({'consumer': consumer, 'topic': topic})
    query = query.copy()
    if last:
        query.update({'_id': {'$gt': last['offset']}})
    collection = mongo.common[topic]

    while True:
        cursor = collection.find(query)
        logging.info(f'{consumer} is iterating over {topic}')
        result = None
        results = await cursor.to_list(length=100)
        for result in results:
            yield result

            await offset.update_one(
                {'consumer': consumer, 'topic': topic},
                {'$set': {'offset': result['_id']}},
                True,
            )
        if result:
            query.update({'_id': {'$gt': result['_id']}})

        if not results:
            logging.info(f'{consumer} to {topic} sub is going to sleep')
            await asyncio.sleep(interval)

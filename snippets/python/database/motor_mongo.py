import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

collection = client.bd.collection

await collection.insert_one({
})

for document in await collection.find().to_list(length=100):
    ...

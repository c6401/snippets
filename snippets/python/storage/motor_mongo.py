import motor.motor_asyncio

mongo = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

collection = mongo.bd.collection

await collection.insert_one({
})

await collection.find_one()

await collection.delete_one({})

for document in await collection.find().to_list(length=100):
    ...

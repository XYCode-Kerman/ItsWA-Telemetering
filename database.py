from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from config import DATABASE_NAME, MONGODB_URI

db = AsyncIOMotorClient(MONGODB_URI)[DATABASE_NAME]


def tel_col() -> AsyncIOMotorCollection:
    return db.get_collection('telemetering')

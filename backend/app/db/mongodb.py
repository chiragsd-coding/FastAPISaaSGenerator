
from motor.motor_asyncio import AsyncIOMotorClient
def get_client(url:str):
    return AsyncIOMotorClient(url)

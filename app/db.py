from motor.motor_asyncio import AsyncIOMotorClient

mongoDB_url: str = "mongodb://127.0.0.1:27017"
database_name: str = "ohmyuchu"

# DB 리소스 관리 객체
class Database:
    # DB connection을 얻어오는 motor의 리소스
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(mongoDB_url)
        cls.db = cls.client[database_name]
    
    
    @classmethod
    async def disconnect(cls):
        if cls.client:
            cls.client.close()

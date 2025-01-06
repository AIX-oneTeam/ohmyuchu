from motor.motor_asyncio import AsyncIOMotorClient
    
# DB 정보
# mongoDB_url: str = "mongodb://192.168.0.141:27017"
# database_name: str = "ohmyuchu"
mongoDB_url: str = "mongodb+srv://ohmyuchu:ohmyuchu1111@test.9r2s8.mongodb.net/"
database_name: str = "test"

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

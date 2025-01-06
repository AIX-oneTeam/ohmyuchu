from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()
    
# DB 정보
mongoDB = os.getenv("mongoDB")
mongoDB_url: str = mongoDB
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

from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection
Mongo_URL = "mongodb://localhost:27017"
DB_NAME = "emotionNarticle"

# app의 생명주기에 mongodb_client와 mongodb를 추가
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션 시작 시 실행되는 코드
    app.mongodb_client = AsyncIOMotorClient(Mongo_URL)
    app.mongodb = app.mongodb_client[DB_NAME]
    print("MongoDB에 연결되었습니다.")
    yield
    # 애플리케이션 종료 시 실행되는 코드
    app.mongodb_client.close()
    print("MongoDB 연결이 종료되었습니다.")

app = FastAPI(lifespan=lifespan)
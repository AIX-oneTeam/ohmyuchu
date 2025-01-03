from pymongo import MongoClient
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수에서 MongoDB 연결 정보 가져오기
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB")

# MongoDB 클라이언트 생성
client = MongoClient(MONGO_URI)

# 데이터베이스 선택
db = client[MONGO_DB_NAME]

# 예제: 컬렉션 선택
collection = db["mycollection"]

# 데이터 삽입 예제
document = {"name": "John", "age": 30}
result = collection.insert_one(document)
print(f"Inserted ID: {result.inserted_id}")

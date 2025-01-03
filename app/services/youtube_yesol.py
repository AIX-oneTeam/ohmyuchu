from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from googleapiclient.discovery import build
from dotenv import load_dotenv

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
import os

# .env 파일 로드
load_dotenv()
# 환경 변수에서 API 키 가져오기
API_KEY = os.getenv("YOUTUBE_API_KEY")
MONGODB_URL=os.getenv("MONGODB_URL")
DATABASE_NAME=os.getenv("DATABASE_NAME")

if not MONGODB_URL or not DATABASE_NAME:
    raise ValueError("Environment variables are missing. Check your .env file.")

# DB 리소스 관리 객체
class Database:
    # DB connection을 얻어오는 motor의 리소스
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        print(f"Connecting to MongoDB with URL: {MONGODB_URL}")
        cls.client = AsyncIOMotorClient(MONGODB_URL)
        if not cls.client:
            raise ValueError("MongoDB client could not be initialized.")
        cls.db = cls.client[DATABASE_NAME]
        print(f"Connected to database: {DATABASE_NAME}")
    
    
    @classmethod
    async def disconnect(cls):
        if cls.client:
            cls.client.close()
            print("Database connection closed")

# Lifespan 핸들러 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to MongoDB...")
    await Database.connect()
    if not Database.client:
        raise ValueError("Database client is not initialized!")
    print("MongoDB connected")
    yield
    print("Disconnecting MongoDB...")
    await Database.disconnect()
    print("MongoDB disconnected")

### fastAPIm jinja템플릿 설정
app = FastAPI(lifespan=lifespan)

# YouTube API 설정
youtube = build("youtube", "v3", developerKey=API_KEY)

@app.get("/ping-db")
async def ping_db():
    try:
        # MongoDB 서버에 핑 테스트
        await Database.client.admin.command("ping")
        return {"status": "success", "message": "MongoDB is connected!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get-all-users")
async def get_all_users():
    collection = Database.db["user"]  # "user" 컬렉션 접근
    cursor = collection.find({})  # 모든 문서 조회
    users = []
    async for document in cursor:  # 비동기적으로 모든 문서를 반복 처리
        document["_id"] = str(document["_id"])  # ObjectId를 문자열로 변환
        users.append(document)
    return {"documents": users}

# 템플릿 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app 디렉토리
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 동영상 검색 (카테고리 아이디가 10이 아니어도 음악 플레이리스트인 경우 있음)
def search_youtube_videos(query, max_results=5):
    request = youtube.search().list(
        q=query,
        part="id,snippet",
        type="video",
        videoCategoryId=10, 
        maxResults=max_results,
    )
    response = request.execute()

    # 동영상 ID 리스트 생성
    video_ids = [item["id"]["videoId"] for item in response.get("items", [])]

    # 동영상 세부 정보 가져오기
    valid_videos = []
    if video_ids:
        video_details = youtube.videos().list(
            part="snippet,status",
            id=",".join(video_ids)
        ).execute()

        for item in video_details.get("items", []):
            # 동영상 상태 확인
            if item["status"]["privacyStatus"] == "public":
                valid_videos.append({
                    "id": item["id"],
                    "title": item["snippet"]["title"],
                    "description": item["snippet"]["description"]
                })

    return valid_videos

@app.get("/music_player", response_class=HTMLResponse)
async def home(request: Request):
    query = "신나는 노래"
    videos = search_youtube_videos(query, max_results=1)
    return templates.TemplateResponse("youtube_yesol.html", {"request": request, "videos": videos})

# # 동영상 카테고리 ID 가져오기
# def get_video_category(video_id):
#     request = youtube.videos().list(
#         part="snippet",
#         id=video_id
#     )
#     response = request.execute()
#     video = response["items"][0]
#     category_id = video["snippet"]["categoryId"]
#     return category_id

# # 카테고리 목록 조회

# def get_video_categories(region_code="US"):
#     request = youtube.videoCategories().list(
#         part="snippet",
#         regionCode=region_code  # 지역 코드 (예: US, KR)
#     )
#     response = request.execute()
#     return response

# # 실행
# categories = get_video_categories("KR")  # 대한민국(KR) 기준
# for item in categories["items"]:
#     print(f"ID: {item['id']}, Title: {item['snippet']['title']}")

# ID: 1, Title: Film & Animation
# ID: 2, Title: Autos & Vehicles
# ID: 10, Title: Music
# ID: 15, Title: Pets & Animals
# ID: 17, Title: Sports
# ID: 18, Title: Short Movies
# ID: 19, Title: Travel & Events
# ID: 20, Title: Gaming
# ID: 21, Title: Videoblogging
# ID: 22, Title: People & Blogs
# ID: 23, Title: Comedy
# ID: 24, Title: Entertainment
# ID: 25, Title: News & Politics
# ID: 26, Title: Howto & Style
# ID: 27, Title: Education
# ID: 28, Title: Science & Technology
# ID: 30, Title: Movies
# ID: 31, Title: Anime/Animation
# ID: 32, Title: Action/Adventure
# ID: 33, Title: Classics
# ID: 34, Title: Comedy
# ID: 35, Title: Documentary
# ID: 36, Title: Drama
# ID: 37, Title: Family
# ID: 38, Title: Foreign
# ID: 39, Title: Horror
# ID: 40, Title: Sci-Fi/Fantasy
# ID: 41, Title: Thriller
# ID: 42, Title: Shorts
# ID: 43, Title: Shows
# ID: 44, Title: Trailers


# import json

# # 보기 좋게 출력
# print(json.dumps(videos, indent=4, ensure_ascii=False))

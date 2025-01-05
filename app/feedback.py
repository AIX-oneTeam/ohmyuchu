from fastapi import FastAPI, Request, HTTPException, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (개발 환경에서만)
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# MongoDB 연결
mongoDB_url: str = "mongodb+srv://ohmyuchu:ohmyuchu1111@test.9r2s8.mongodb.net/"
database_name: str = "test"

client = MongoClient(mongoDB_url)
db = client[database_name]  # 데이터베이스 이름
songs_collection = db['songs']  # 컬렉션 이름
analysis_collection =  db['analysis']

# emotion = "기쁨"
# random_song = songs_collection.aggregate([
#     {"$match": {"emotion": emotion}},  # 감정에 맞는 노래만 필터링
#     {"$sample": {"size": 1}}  # 랜덤으로 1개의 노래 선택
# ])

# song = list(random_song)
# song[0]['title']

@app.get("/song/")
def get_song_data(request:Request, emotion:str) :
    # 감정에 해당하는 노래 중에서 랜덤으로 하나 선택
    random_song = songs_collection.aggregate([
        {"$match": {"emotion": emotion}},  # 감정에 맞는 노래만 필터링
        {"$sample": {"size": 1}}  # 랜덤으로 1개의 노래 선택
    ])
    
    # 결과가 있으면 반환
    song = list(random_song)
    
    if song:
        # 노래 정보 반환
        selected_song = song[0]
        song_data = {
            "title": selected_song["title"],
            "artist": selected_song["artist"],
            "src": selected_song["src"]
        }

        songs_collection.update_one(
            {"title": selected_song["title"]},
            {"$inc": {"like_count": 1}}
        )

        analysis_collection.update_one(
            {"title": selected_song["title"]},
            {"$inc": {"total_play_count": 1,
                      f"emotion_summary.{emotion}": 1}}
        )

        return templates.TemplateResponse("/feedback.html", {
         "request": request,
         "song": song_data
    })
    else:
        return "알 수 없는 감정입니다."


@app.post("/like")
async def increase_like(data: dict = Body(...)):
    print(f"Received data: {data}")  # 요청 데이터 확인
    title = data.get("title")
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    
    result = songs_collection.update_one(
        {"title": title},
        {"$inc": {"like_count": 1}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Song not found")
    
    return {"message": "Like count updated successfully"}

@app.post("/dislike")
async def decrease_dislike(data: dict = Body(...)):
    print(f"Received data: {data}")  # 요청 데이터 확인
    title = data.get("title")
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    
    result = songs_collection.update_one(
        {"title": title},
        {"$inc": {"dislike_count": 1}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Song not found")
    
    return {"message": "disLike count updated successfully"}


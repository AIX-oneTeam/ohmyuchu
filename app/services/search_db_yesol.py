from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import random

app = FastAPI()

# MongoDB 설정
mongoDB_url = "mongodb://192.168.0.141:27017"
database_name = "ohmyuchu"

# MongoDB 클라이언트 초기화
client = MongoClient(mongoDB_url)
db = client[database_name]
songs_collection = db["songs"]
comments_collection = db["comments"]
emotion="분노"
@app.get("/song/{emotion}")
async def get_random_song(emotion: str):
    songs = list(songs_collection.find({"emotion": emotion}))
    if not songs:
        raise HTTPException(status_code=404, detail=f"No songs found with emotion '{emotion}'")
    
    random_song = random.choice(songs)
    return {
        "title": random_song.get("title", "정보 없음"),
        "artist": random_song.get("artist", "정보 없음"),
        "url": random_song.get("url", "정보 없음")
    }

@app.get("/comment/{emotion}")
async def get_random_comment(emotion: str):
    comments = list(comments_collection.find({"emotion": emotion}))
    if not comments:
        raise HTTPException(status_code=404, detail=f"No songs found with emotion '{emotion}'")
    
    random_comment= random.choice(comments[0]['comments'])
    return {
        "comment": random_comment if random_comment else "정보 없음"    }


from typing import Union
from services.emotion_service import analyze_emotion 
from fastapi import FastAPI, Form, Request, HTTPException, Body
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests import request
from services.crawling_service import crawlingfromUrl
from services.music_service import get_song_data
from db import Database

# FastAPI의 APIRouter를 kakao_controller.py에 import하여 router 객체 생성
from kakao_controller import router as kakao_router

db = Database()
songs_collection = db['songs']  
analysis_collection = db['analysis']
# 뷰 템플릿이 위치한 경로 지정
templates = Jinja2Templates(directory="templates")

@asynccontextmanager
async def lifespan(app: FastAPI ):
    print("Connencting DataBase")
    await db.connect() 
    app.mongodb = db.client["ohmyuchu"]    

    yield
    # print("Disconnecting DataBase")
    # await db.disconnect()
    
app = FastAPI(lifespan=lifespan)

# 정적 파일 경로 추가 
app.mount("/static", StaticFiles(directory="static"), name="static")

# Kakao 라우터 등록
app.include_router(kakao_router, prefix="/auth/kakao")

# 메인 페이지
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
#결과 페이지
@app.get("/result", response_class=HTMLResponse)
async def read_result(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})

@app.post("/v1/models/summary")
async def summarization(request: Request, url: str = Form(...)):
    summary = crawlingfromUrl(url)
    emotion = analyze_emotion(summary['summary'])
    music = get_song_data(emotion)
    data = {
        "summary": summary['summary'],
        "emotion": emotion,
        "music":{
            "title": music['title'],
            "artist": music['artist'],
            "src": music['src']
        }
    }

    return templates.TemplateResponse("result.html", {"request": request, "data": data})

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


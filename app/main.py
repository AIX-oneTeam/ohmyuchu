from typing import Union
from services.day_count_service import print_day_count, save_day_count
from services.emotion_service import analyze_emotion 
from fastapi import FastAPI, Form, Request, HTTPException, Body
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests import request
from services.crawling_service import crawlingfromUrl
from services.music_service import get_song_data
from services.comment_service import get_comment
from db import Database


# FastAPI의 APIRouter를 kakao_controller.py에 import하여 router 객체 생성
from kakao_controller import router as kakao_router

db = Database()
# 뷰 템플릿이 위치한 경로 지정
templates = Jinja2Templates(directory="templates")

@asynccontextmanager
async def lifespan(app: FastAPI ):
    print("Connencting DataBase")
    await db.connect() 
    app.mongodb = db.client["test"]    

    yield
    print("Disconnecting DataBase")
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

# 정적 파일 경로 추가
app.mount("/static", StaticFiles(directory="static"), name="static")

# Kakao 라우터 등록
app.include_router(kakao_router, prefix="/auth/kakao")

# 메인 페이지
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    count_data = await print_day_count()
    return templates.TemplateResponse("index.html", {"request": request, "count_data": count_data})

# @app.get("/result", response_class=HTMLResponse)
# async def read_result(request: Request):
#     return templates.TemplateResponse("result.html", {"request": request, "data": data})

@app.post("/v1/models/summary")
async def summarization(request: Request, userInfo: str = Form(...), url: str = Form(...)):
    songs_collection = Database.db['songs']
    analysis_collection = Database.db['analysis']
    comment_collection = Database.db['comment']

    print(f"Received URL: {userInfo}")  # 요청 URL 확인

    # 1) 크롤링 시도
    try:
        summary = crawlingfromUrl(url)  # dict 형태를 기대
        # summary['summary']가 없으면 KeyError가 날 수 있으므로 아래에서도 감싸기
        main_summary = summary['summary']
    except KeyError:
        # summary['summary'] 키가 없으면 => 잘못된 url이거나 크롤링 실패
        content = """
        <script>
            alert("유효하지 않은 URL이거나 처리할 수 없습니다. 다시 입력해주세요!");
            window.location.href = "/";
        </script>
        """
        return HTMLResponse(content=content, status_code=200)
    except Exception as e:
        # 그 외 모든 예외 처리 (requests 에러, 등등)
        content = f"""
        <script>
            alert("에러가 발생했습니다: {str(e).replace('"','\\"')}");
            window.location.href = "/";
        </script>
        """
        return HTMLResponse(content=content, status_code=200)

    # 2) 정상적으로 수집된 경우 처리
    emotion = analyze_emotion(main_summary)
    music = await get_song_data(emotion, songs_collection, analysis_collection)
    #감정에 따른 랜덤 코멘트 가져오기
    comment = await get_comment(emotion, comment_collection )

    data = {
        "summary": main_summary,
        "emotion": emotion,
        "comment": comment,
        "music":{
            "title": music['title'],
            "artist": music['artist'],
            "src": music['src']
        }
    }
    return templates.TemplateResponse("result.html", {"request": request, "data": data})

@app.post("/like")
async def increase_like(data: dict = Body(...)):
    songs_collection = Database.db['songs']  
    analysis_collection = Database.db['analysis']

    print(f"Received data: {data}")  # 요청 데이터 확인
    title = data.get("title")
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    
    result = await songs_collection.update_one(
        {"title": title},
        {"$inc": {"like_count": 1}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Song not found")
    
    return {"message": "Like count updated successfully"}

@app.post("/dislike")
async def decrease_dislike(data: dict = Body(...)):
    songs_collection = Database.db['songs']  
    analysis_collection = Database.db['analysis']
    print(f"Received data: {data}")  # 요청 데이터 확인
    title = data.get("title")
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    
    result = await songs_collection.update_one(
        {"title": title},
        {"$inc": {"dislike_count": 1}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Song not found")
    
    return {"message": "disLike count updated successfully"}

@app.post("/addCount")
async def addCount(userInfo: dict = Body(...)):
    # userInfo를 받아 DB에 저장하는 메서드
    # userInfo에 이미 로그인 여부 정보 담겨있음.
    # 비회원일 경우 email = anaonymous, nickname = anonymous
    print("userInfo: ", userInfo) 
    save_day_count(userInfo)

from typing import Union
from fastapi import FastAPI, Form, Request
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests import request
from services.crawling_service import crawlingfromUrl
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
    data = crawlingfromUrl(url)

    return templates.TemplateResponse("result.html", {"request": request, "summary": data['summary']})


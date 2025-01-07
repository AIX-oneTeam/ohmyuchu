from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()
mongoDB = os.getenv("mongoDB")

app = FastAPI()

client = MongoClient(mongoDB)  # 기본 로컬 MongoDB 서버에 연결
db = client['test']  # 사용할 데이터베이스 이름
collection = db['songs']  # 사용할 컬렉션 이름 

templates = Jinja2Templates(directory="templates")



# 감정을 변수로 받아 해당하는 플레이리스트의 가수,제목, 연결url를 리턴하는 함수
@app.get("/song/")
def get_song_data(request:Request, emotion:str) :
    # 감정에 해당하는 노래 중에서 랜덤으로 하나 선택
    random_song = collection.aggregate([
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

        return templates.TemplateResponse("/result.html", {
         "request": request,
         "song": song_data
    })
    else:
        return "알 수 없는 감정입니다."
    


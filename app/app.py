from fastapi import FastAPI, HTTPException
from data_models import User
from typing import List

app = FastAPI()
db = get_database()

# 전체 유저의 정보들을 리스트로 반환
@app.get("/users", response_model=List[User])
async def read_users(user_id: int):
    user = await 



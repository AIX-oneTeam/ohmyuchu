# main.py
from fastapi import FastAPI
# 어플리케이션의 생명주기를 관리하는 모듈
from contextlib import asynccontextmanager
from fastapi.params import Depends
from bson import ObjectId
from db import Database

db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI ):
    print("Connencting DataBase")
    await db.connect() 
    app.mongodb = db.client["ohmyuchu"]    

    yield
    # print("Disconnecting DataBase")
    # await db.disconnect()
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    users = await app.mongodb["user"].find().to_list(length=100)
    if users is None:
        return {"message": "No user found"}
    for user in users:
        user["_id"] = str(user["_id"])
    return users





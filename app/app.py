from typing import Union
from fastapi import FastAPI
from contextlib import asynccontextmanager
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

@app.post("/user")
async def create_user(user: dict):
    result = await app.mongodb["user"].insert_one(user)
    return {"_id": str(result.inserted_id)}
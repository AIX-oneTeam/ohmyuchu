from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    id: int = Field(default=None, alias="_id")
    text: str
    emotions: List[str] = []

    

    
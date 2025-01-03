from pydantic import BaseModel, Field


class comment(BaseModel):
    id: int = Field(default=None, alias="_id")
    EmotionId: int
    text: str
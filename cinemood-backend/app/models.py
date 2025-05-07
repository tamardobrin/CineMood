from pydantic import BaseModel

class MoodInput(BaseModel):
    reason: str

class MovieRecommendation(BaseModel):
    title: str
    overview: str
    reason: str

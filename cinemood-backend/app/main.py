from fastapi import FastAPI
from app.models import MoodInput, MovieRecommendation
from app.nlp import extract_mood_tags
from app.recommender import recommend_movies

app = FastAPI()

@app.post("/recommend", response_model=list[MovieRecommendation])
def recommend(input: MoodInput):
    tags = extract_mood_tags(input.reason)
    print("Extracted Tags:", tags)
    return recommend_movies(tags)


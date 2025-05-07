import httpx
import os
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

TMDB_BASE_URL = "https://api.themoviedb.org/3"

async def search_movies_by_keywords(keywords: list[str]) -> list[dict]:
    movies = []
    async with httpx.AsyncClient() as client:
        for keyword in keywords:
            response = await client.get(
                f"{TMDB_BASE_URL}/search/movie",
                params={
                    "api_key": TMDB_API_KEY,
                    "query": keyword,
                    "include_adult": False,
                    "language": "en-US"
                }
            )
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])[:3]  # Top 3 per keyword
                for result in results:
                    movies.append({
                        "title": result["title"],
                        "overview": result.get("overview", ""),
                        "match_reason": f"Related to '{keyword}'"
                    })
    return movies

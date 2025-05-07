from app.models import MovieRecommendation
from app.tmdb_client import search_movies_by_keywords
import asyncio

def recommend_movies(tags: list[str]) -> list[MovieRecommendation]:
    results = asyncio.run(search_movies_by_keywords(tags))

    recommendations = []
    for movie in results[:5]:  # Limit to 5 overall
        recommendations.append(MovieRecommendation(
            title=movie["title"],
            overview=movie["overview"],
            reason=movie["match_reason"]
        ))

    if not recommendations:
        recommendations.append(MovieRecommendation(
            title="Paddington 2",
            overview="A bear teaches humans kindness. What more do you need?",
            reason="Default pick — just in case nothing matched!"
        ))

    return recommendations

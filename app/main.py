from fastapi import FastAPI
from app.models import PromptRequest, RecommendationResponse, Anime

app = FastAPI()

@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(prompt: PromptRequest):
    return RecommendationResponse(results=[
        Anime(
            title="Shingeki no Kyojin",
            explanation="Highly emotional and action-packed, fits your mood perfectly.",
            genres=["Action", "Drama", "Fantasy"],
            episodes=25,
            rating=8.47,
            ranked=111,
            aired="Apr 7, 2013 to Sep 29, 2013",
            synopsis="Centuries ago, mankind was slaughtered to near extinction by titans...",
            img_url="https://cdn.myanimelist.net/images/anime/10/47347.jpg"
        ),
        Anime(
            title="Clannad",
            explanation="Deeply emotional and touching story of family and personal growth.",
            genres=["Drama", "Romance", "Slice of Life"],
            episodes=23,
            rating=8.00,
            ranked=301,
            aired="Oct 4, 2007 to Mar 27, 2008",
            synopsis="Okazaki Tomoya is a delinquent who finds life dull and believes he'll never amount to anything...",
            img_url="https://cdn.myanimelist.net/images/anime/10/21899.jpg"
        )
    ])

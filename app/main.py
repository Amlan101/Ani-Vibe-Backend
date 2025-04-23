from fastapi import FastAPI
from app.recommender import get_recommendations
from app.models import PromptRequest, RecommendationResponse

app = FastAPI()

@app.post("/recommendations", response_model=RecommendationResponse)
def recommend(prompt: PromptRequest):
    try:
        results = get_recommendations(prompt.prompt)
        return RecommendationResponse(results=results)
    except ValueError as e:
        return RecommendationResponse(results=[])
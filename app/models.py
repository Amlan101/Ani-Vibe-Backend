from pydantic import BaseModel
from typing import List, Optional

class PromptRequest(BaseModel):
    prompt: str

class Anime(BaseModel):
    title: str
    explanation: str
    genres: List[str] = []
    episodes: Optional[float] = None
    rating: Optional[float] = None
    ranked: Optional[float] = None
    aired: Optional[str] = None
    synopsis: Optional[str] = None
    img_url: Optional[str] = None

class RecommendationResponse(BaseModel):
    results: List[Anime]
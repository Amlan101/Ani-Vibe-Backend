import pandas as pd

df = pd.read_csv("data/anime_dataset_with_sentiment.csv")

df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')

def mood_to_sentiment(prompt: str):
    prompt = prompt.lower()
    mapping = {
        'happy': (0.1, 1.0),
        'sad': (-1.0, -0.1),
        'excited': (0.5, 1.0),
        'relaxed': (0.0, 0.5),
        'angry': (-1.0, -0.5),
        'nostalgic': (0.0, 0.5),
        'adventurous': (0.3, 1.0),
        'romantic': (0.2, 1.0),
        'melancholic': (-0.5, 0.0),
        'motivated': (0.3, 1.0),
        'curious': (0.0, 1.0),
        'hopeful': (0.2, 1.0),
        'bored': (-0.5, 0.0),
        'fearful': (-1.0, -0.3),
        'confused': (-0.5, 0.0),
        'pensive': (0.0, 0.5),
        'playful': (0.3, 1.0),
        'determined': (0.3, 1.0),
        'surprised': (0.0, 1.0),
        'skeptical': (-0.5, 0.0),
        'grateful': (0.2, 1.0),
        'lonely': (-1.0, -0.1),
        'content': (0.0, 0.5),
        'anxious': (-1.0, -0.3),
        'empowered': (0.3, 1.0),
        'silly': (0.3, 1.0),
        'reflective': (0.0, 0.5),
        'inspired': (0.3, 1.0),
        'disappointed': (-0.5, 0.0),
        'peaceful': (0.0, 0.5),
        'confident': (0.1, 0.8),
        'sexy': (0.0, 0.5),
        'energetic': (0.3, 1.0),
        'nonchalant': (-0.8, 0.0),
        'suicidal': (0.5, 1.0),
        'shocked': (0.0, 0.5),
        'passionate': (0.3, 1.0),
        'nothing': (-1, 1),
        'optimistic': (0.3, 1.0),
        'gloomy': (-0.8, -0.2),
        'grumpy': (-0.6, -0.1),
        'elated': (0.7, 1.0),
        'tense': (-0.7, -0.2),
        'embarrassed': (-0.5, 0.0),
        'jealous': (-0.6, -0.1),
        'blissful': (0.5, 1.0),
        'apathetic': (-0.5, 0.0),
        'awed': (0.4, 1.0),
        'vindicated': (0.4, 1.0),
        'resentful': (-0.6, -0.2),
        'ecstatic': (0.8, 1.0),
        'frustrated': (-0.7, -0.2),
        'ashamed': (-0.6, -0.1),
        'powerful': (-0.9, -0.5),
        'destructive': (-0.7, -0.5),
        'low': (-0.5, 0.0),
        'emotional' : (-0.5, 0.5),
        'laugh' : (0.3, 1.0),
        'uplifting': (0.5, 1.0),
    }
    
    for mood in mapping:
        if mood in prompt:
            return mapping[mood]
    
    return None

def get_recommendations(mood: str, top_k: int = 15):
    sentiment_range = mood_to_sentiment(mood)
    if not sentiment_range:
        raise ValueError("Mood not recognized")

    lower, upper = sentiment_range

    recommendations = df[(df['sentiment'] >= lower) & (df['sentiment'] <= upper)]

    if recommendations.empty:
        return []

    recommendations = recommendations.head(top_k)

    results = []
    for _, row in recommendations.iterrows():
        results.append({
            "title": row.get("title"),
            "explanation": f"This anime matches the '{mood}' mood range.",
            "genres": row.get("genre", "").split(", ") if pd.notna(row.get("genre")) else [],
            "episodes": row.get("episodes"),
            "rating": row.get("score"),
            "ranked": row.get("ranked"),
            "aired": row.get("aired"),
            "synopsis": row.get("synopsis"),
            "img_url": row.get("img_url")
        })

    return results

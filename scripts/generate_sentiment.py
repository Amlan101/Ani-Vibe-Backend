import pandas as pd
from textblob import TextBlob
from tqdm import tqdm

df = pd.read_csv("data/animes_recommender_data.csv")

tqdm.pandas()

def compute_sentiment(text):
    if pd.isna(text) or not isinstance(text, str):
        return 0.0
    return TextBlob(text).sentiment.polarity 

df['sentiment'] = df['synopsis'].progress_apply(compute_sentiment)

df.to_csv("data/anime_dataset_with_sentiment.csv", index=False)

print("Sentiment values added and dataset saved!")


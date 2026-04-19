from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load data
movies = pd.read_csv('data/movies.csv')
movies['genres'] = movies['genres'].fillna('')

# Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# API route
@app.get("/recommend")
def recommend(movie: str):
    if movie not in indices:
        return {"error": "Movie not found"}
    
    idx = indices[movie]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    
    recommendations = movies['title'].iloc[movie_indices].tolist()
    
    return {"recommendations": recommendations}
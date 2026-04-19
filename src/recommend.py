import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv('data/movies.csv')

# Fill missing genres
movies['genres'] = movies['genres'].fillna('')

# Convert text to vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index
movies = movies.reset_index()

# Function to recommend movies
def recommend(movie_title):
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()
    
    if movie_title not in indices:
        return "Movie not found"
    
    idx = indices[movie_title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]  # Top 5
    
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices]

# Test
print(recommend("Toy Story (1995)"))
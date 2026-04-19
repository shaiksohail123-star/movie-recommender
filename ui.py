import streamlit as st
import pandas as pd
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔑 TMDB API KEY (paste your real key here)
API_KEY = "c1950dd9794d8fcaa8d273ecbd3902dd"

st.set_page_config(page_title="Movie Recommender", layout="centered")

# 📥 Load data
movies = pd.read_csv("data/movies.csv")
movies['genres'] = movies['genres'].fillna('')

# 🎬 UI
st.title("🎬 Movie Recommender")
st.write("Get personalized movie suggestions")
st.divider()

# 🎯 Build model
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# 🤖 Recommendation function
def recommend(movie):
    if movie not in indices:
        return []

    idx = indices[movie]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].tolist()

# 🧠 Normalize title (important fix)
def normalize_title(title):
    title = title.split('(')[0].strip()

    # Fix ", The"
    if title.endswith(", The"):
        title = "The " + title[:-5]
    elif title.endswith(", A"):
        title = "A " + title[:-3]
    elif title.endswith(", An"):
        title = "An " + title[:-4]

    # Remove problematic characters
    title = title.replace(",", "")
    title = title.replace(".", "")
    title = title.replace(":", "")
    
    return title.strip()

# 🎥 Fetch poster
def fetch_poster(movie):
    try:
        title = normalize_title(movie)
        year = movie.split('(')[-1].replace(')', '').strip()

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}&year={year}"

        data = requests.get(url, timeout=5).json()

        best_match = None
        max_votes = 0

        for result in data.get("results", []):
            votes = result.get("vote_count", 0)

            if result.get("poster_path") and votes > max_votes:
                best_match = result
                max_votes = votes

        if best_match:
            return f"https://image.tmdb.org/t/p/w500{best_match['poster_path']}"

    except:
        return None

    return None

# 🎛️ UI input
movie_name = st.selectbox("Choose a movie:", movies['title'].values)

# 🚀 Button
if st.button("✨ Recommend"):
    recommendations = recommend(movie_name)

    if recommendations:
        st.subheader("🎯 Recommended for you")

        cols = st.columns(5)

        DEFAULT_POSTER = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

        for i, movie in enumerate(recommendations):
            with cols[i % 5]:
                poster = fetch_poster(movie)

                if poster:
                    st.image(poster)
                else:
                    st.image(DEFAULT_POSTER)

                st.caption(movie)

    else:
        st.error("Movie not found")
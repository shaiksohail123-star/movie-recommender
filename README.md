# 🎬 Movie Recommender System

A content-based movie recommendation system built using Machine Learning and deployed with Streamlit. This app suggests similar movies based on user selection and displays movie posters using the TMDB API.

---

## 🚀 Live Demo

👉 https://movie-recommender-zgswa9rj2mxrcwkrnhtdbb.streamlit.app

---

## 📸 Screenshots

### 🏠 Home Page

<img width="1920" height="925" alt="moive before search" src="https://github.com/user-attachments/assets/c7d85795-6b68-45a8-b4e0-e0c9a6f3d45b" />


### 🎯 Recommendations

<img width="1920" height="923" alt="moive after search" src="https://github.com/user-attachments/assets/90541416-b8eb-4e0c-8702-6cc810541bad" />


---

## ✨ Features

* 🎥 Select a movie and get similar recommendations
* 🧠 Content-based filtering using TF-IDF + Cosine Similarity
* 🖼️ Movie posters fetched using TMDB API
* ⚡ Fast and interactive UI with Streamlit
* 🌐 Fully deployed web application

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* TMDB API

---

## 🧠 How It Works

1. Movie genres are processed using **TF-IDF Vectorization**
2. Similarity between movies is calculated using **Cosine Similarity**
3. Top similar movies are recommended
4. Posters are fetched dynamically using TMDB API

---

## 📁 Project Structure

```
movie-recommender/
│
├── data/
│   └── movies.csv
│
├── ui.py
├── recommend.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/shaiksohail123-star/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add TMDB API key

Create `.streamlit/secrets.toml`:

```
API_KEY = "c1950dd9794d8fcaa8d273ecbd3902dd"
```

### 4. Run the app

```
streamlit run ui.py
```

---

## 🔐 API Used

* TMDB (The Movie Database) API
  https://www.themoviedb.org/

---

## 📌 Future Improvements

* 🔍 Search-based recommendations
* ⭐ Show movie ratings
* 🎭 Filter by genre
* 🤖 Advanced recommendation using NLP / embeddings

---

## 🙌 Author

**Sohail**
Aspiring Data Scientist / Data Analyst

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and share it!


🎬 Cinema Now Dashboard

A visualization-driven movie analytics dashboard built with Python + Streamlit.
Users can search for any movie and instantly explore ratings, streaming availability, regional interest, and sentiment from user reviews.

🚀 Features

🔍 Movie Search – Search any movie using TMDB

📝 Synopsis & Metadata – Overview, runtime, genres, release date

⭐ Ratings Comparison – IMDb, Rotten Tomatoes, Metacritic (visualized)

📊 Ratings Chart – Normalized comparison across platforms

📺 Where to Watch – Streaming / Rent / Buy platforms by region

🌍 Regional Interest – Audience interest inferred from regional metadata

💬 Reviews & Sentiment – User reviews with sentiment analysis

🎨 Clean UI – Structured layout with clear sections

🧠 Tech Stack

Frontend / UI: Streamlit

Backend: Python

APIs:

TMDB (movies, streaming providers, reviews)

OMDb (ratings)

Visualization: Plotly

Sentiment Analysis: TextBlob

🏗️ Project Structure
Cinema-Now-Dashboard/
├── backend/
│   ├── app.py
│   └── utils/
│       ├── tmdb_api.py
│       ├── omdb_api.py
│       └── sentiment.py
│
├── frontend/
│   └── src/
│       └── .gitkeep
│
├── database/
│   └── .gitkeep
│
├── .gitignore
├── requirements.txt
├── README.md

🌍 Deployment

This app is deployed using Streamlit Community Cloud.

Live Demo: https://cinema-now-dashboard.streamlit.app/

## 📸 Screenshots

### Home Page
![Movie Overview](Cinema-Now-Dashboard\screenshots\Home Page.png)

### Platforms
![Ratings](Cinema-Now-Dashboard\screenshots\Platforms.png)

### Reviews & Sentiment
![Reviews](Cinema-Now-Dashboard\screenshots\Reviews.png)

### Ratings Graph
![Ratings Graph](Cinema-Now-Dashboard\screenshots\Ratings Graph.png)

### Search
![Ratings](Cinema-Now-Dashboard\screenshots\Search.png)

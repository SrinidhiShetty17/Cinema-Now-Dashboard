import streamlit as st
import sys
import os
from dotenv import load_dotenv
from utils.omdb_api import get_ratings
from visuals.charts import ratings_bar_chart
from utils.tmdb_api import get_streaming_providers
from utils.tmdb_api import get_trending_regions
from utils.tmdb_api import get_movie_reviews
from utils.sentiment import analyze_sentiment

# -------------------------------------------------
# Fix Python path 
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(PROJECT_ROOT)

from utils.tmdb_api import search_movie, get_movie_details
load_dotenv()
st.set_page_config(
    page_title="Cinema Now Dashboard",
    layout="wide"
)

st.title("🎬 Cinema Now")
st.subheader("Search movies. Compare ratings. Explore streaming platforms.")

st.markdown(
    """
    Welcome to **Cinema Now Dashboard** 🎥  
    Search for a movie and explore its details.
    """
)

# Movie Search Form 
with st.form("movie_search_form"):
    movie_name = st.text_input("Enter a movie name")
    submitted = st.form_submit_button("Search")

# Handle Search
if submitted and movie_name:
    movie = search_movie(movie_name)

    if movie:
        details = get_movie_details(movie["id"])

        if not details:
            st.error("Unable to fetch movie details. Please try again.")
            st.stop()

        col1, col2 = st.columns([1, 2])

        # Poster
        with col1:
            if details.get("poster_path"):
                poster_url = f"https://image.tmdb.org/t/p/w500{details['poster_path']}"
                st.image(poster_url, width=300)
            else:
                st.info("Poster not available")

        # Movie Details
        with col2:
            st.subheader(details.get("title", "Title not available"))
            st.write(details.get("overview", "No overview available."))

            st.markdown(f"**Release Date:** {details.get('release_date', 'N/A')}")
            st.markdown(f"**Runtime:** {details.get('runtime', 'N/A')} minutes")

            genres = [g["name"] for g in details.get("genres", [])]
            if genres:
                st.markdown(f"**Genres:** {', '.join(genres)}")
            else:
                st.markdown("**Genres:** N/A")
       # --- Ratings ---
            ratings = get_ratings(
                title=details.get("title"),
                year=(details.get("release_date", "")[:4] or None)
            )

            st.markdown("### ⭐ Ratings")

            if ratings:
                chart = ratings_bar_chart(ratings)
                if chart:
                    st.plotly_chart(chart, use_container_width=True)
                else:
                    st.write("Ratings available, but could not be visualized.")
            else:
                st.write("Ratings not available.")
        # --- Streaming Platforms ---
            st.markdown("### 📺 Where to Watch")

            region = st.selectbox("Region", ["IN", "US"])

            providers = get_streaming_providers(
                movie_id=details["id"],
                region=region
            )

            if providers:
                if providers["streaming"]:
                    st.markdown("**Streaming:**")
                    for p in providers["streaming"]:
                        st.write(f"• {p}")

                if providers["rent"]:
                    st.markdown("**Rent:**")
                    for p in providers["rent"]:
                        st.write(f"• {p}")

                if providers["buy"]:
                    st.markdown("**Buy:**")
                    for p in providers["buy"]:
                        st.write(f"• {p}")

                if not any(providers.values()):
                    st.write("No availability information for this region.")
            else:
                st.write("No availability information for this region.")
        # --- Regional Interest ---
            st.markdown("### 🌍 Regions with High Audience Interest")

            trending_regions = get_trending_regions(details)

            if trending_regions:
                for region in trending_regions:
                    st.write(f"• {region}")
            else:
                st.write("Audience interest data not available.")
        # --- Reviews & Sentiment ---
            st.markdown("### 📝 Reviews & Sentiment")

            reviews = get_movie_reviews(details["id"])

            if reviews:
                sentiment_summary = {"Positive": 0, "Neutral": 0, "Negative": 0}

                for review in reviews:
                    content = review.get("content", "")
                    author = review.get("author", "Anonymous")

                    sentiment, score = analyze_sentiment(content)
                    sentiment_summary[sentiment] += 1

                    with st.expander(f"Review by {author} ({sentiment})"):
                        st.write(content[:800] + ("..." if len(content) > 800 else ""))
                        st.caption(f"Sentiment score: {round(score, 2)}")

                st.markdown("#### Overall Sentiment")
                for k, v in sentiment_summary.items():
                    st.write(f"{k}: {v}")

            else:
                st.write("No reviews available.")


elif submitted:
    st.error("Movie not found. Try another title.")

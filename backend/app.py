import streamlit as st
import sys
import os
from dotenv import load_dotenv
from utils.omdb_api import get_ratings
from visuals.charts import ratings_bar_chart



# -------------------------------------------------
# Fix Python path so utils can be imported
# -------------------------------------------------
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

                
elif submitted:
    st.error("Movie not found. Try another title.")

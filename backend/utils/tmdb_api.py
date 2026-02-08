import os
import httpx
from pathlib import Path
from dotenv import load_dotenv

# -------------------------------------------------
# Load .env explicitly from PROJECT ROOT
# -------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_PATH)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def search_movie(movie_name: str):
    """
    Search for a movie by name and return the top TMDB result.
    """
    if not TMDB_API_KEY or not movie_name:
        return None

    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name,
        "language": "en-US",
        "include_adult": False,
    }

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        results = data.get("results", [])
        return results[0] if results else None

    except httpx.HTTPError:
        return None


def get_movie_details(movie_id: int):
    """
    Fetch full movie details using TMDB movie ID.
    """
    if not TMDB_API_KEY or not movie_id:
        return None

    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
    }

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError:
        return None

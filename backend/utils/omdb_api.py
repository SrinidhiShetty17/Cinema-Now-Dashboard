import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_PATH)

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "https://www.omdbapi.com/"


def get_ratings(title: str, year: str | None = None):
    if not OMDB_API_KEY or not title:
        return {}

    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
    }
    if year:
        params["y"] = year

    try:
        with httpx.Client(timeout=10.0) as client:
            r = client.get(BASE_URL, params=params)
            r.raise_for_status()
            data = r.json()

        ratings = {}
        for item in data.get("Ratings", []):
            ratings[item["Source"]] = item["Value"]

        return ratings

    except httpx.HTTPError:
        return {}

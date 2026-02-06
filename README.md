# Cinema-Now-Dashboard
Search and explore movies with synopsis, ratings, streaming platforms, trends, and review

## Overview
A user-driven movie exploration system that aggregates movie metadata,
ratings, streaming availability, trending regions, and reviews using
multiple public APIs.

## Problem Statement
Movie information is fragmented across platforms like IMDb, Netflix,
and Rotten Tomatoes. Users lack a unified interface to explore a movie’s
performance, availability, and audience sentiment.

## System Architecture
- Backend: Python + Streamlit
- APIs: TMDB, OMDb
- Visualization: Plotly, Matplotlib
- Sentiment Analysis: TextBlob

## Features
- Movie search by name
- Synopsis and metadata
- Cross-platform ratings
- Streaming platform availability
- Trending regions (proxy metrics)
- Audience reviews and sentiment

## Project Structure
```text
backend/
frontend/
database/

"""
Configuration settings for the application.
This module defines eight main audio features and sets u basic configuration variables.
"""

import os
from pathlib import Path

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the path to the database file
DATABASE_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATABASE_DIR / "raw"
PROCESSED_DATA_DIR = DATABASE_DIR / "processed"
SAMPLE_DATA_DIR = DATABASE_DIR / "sample"

#Define audio features
AUDIO_FEATURES = [
    "energy",
    "danceability",
    "valence",
    "tempo",
    "acousticness",
    "instrumentalness",
    "liveness",
    "speechiness",
]

#Add Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "your_spotify_client_id")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "your_spotify_client_secret")   
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

#Add visualization settings
VISUALIZATION_SETTINGS = {
    "plot_style": "seaborn-v0_8",
    "figure_size": (10, 6),
    "font_size": 12,
    "color_palette": "viridis",
    "line_width": 2,
    "marker_style": "o",
    "grid": True,
    "legend": True,
    "title": "Visualization of Your Music Taste",
    "xlabel": "Time",
    "ylabel": "Feature Value",
}



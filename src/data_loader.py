"""
Sample data loader for audio features and tempo.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import configuration settings
from config.config import AUDIO_FEATURES, SAMPLE_DATA_DIR

#Data generator function structure
def create_sample_data():
    """
    Create Spotify-like sample data for development of app.
    """
    np.random.seed(42) #for reproductibility

    #Define number of tracks
    num_personal_tracks = 500
    num_global_tracks = 1000

    #Create personal data
    personal_data = {
        'track_id': [f'track_{i}' for i in range(num_personal_tracks)],
        'energy': np.random.beta(2, 2, num_personal_tracks),
        'danceability': np.random.beta(2, 2, num_personal_tracks),
        'valence': np.random.beta(2, 2, num_personal_tracks),
        'tempo': np.random.normal(120, 30, num_personal_tracks),
        'acousticness': np.random.beta(1, 3, num_personal_tracks),
        'instrumentalness': np.random.beta(1, 5, num_personal_tracks),
        'liveness': np.random.beta(1, 4, num_personal_tracks),
        'speechiness': np.random.beta(1, 4, num_personal_tracks),
        'artist': [f'artist_{i % 50}' for i in range(num_personal_tracks)],
        'album': [f'album_{i % 20}' for i in range(num_personal_tracks)],
        'genre': np.random.choice(['Pop', 'Rock', 'Hip-Hop', 'Indie', 'Electronic', 'Jazz'], num_personal_tracks, p=[0.3, 0.2, 0.2, 0.1, 0.1, 0.1]),
        'play_count': np.random.poisson(5, num_personal_tracks)+1,
        'skip_count': np.random.poisson(2, num_personal_tracks),
    }
    #Create global data
    global_data = {
        'track_id': [f'global_track_{i}' for i in range(num_global_tracks)],
        'artist': [f'global_artist_{i % 100}' for i in range(num_global_tracks)],
        'album': [f'global_album_{i % 150}' for i in range(num_global_tracks)],
        'genre': np.random.choice(['Pop', 'Rock', 'Hip-Hop', 'Indie', 'Electronic', 'Jazz'], num_global_tracks, p=[0.4, 0.15, 0.15, 0.1, 0.1, 0.1]),
        'popularity': np.random.beta(2,2,num_global_tracks)*100,
        'energy': np.random.beta(2, 2, num_global_tracks),
        'tempo': np.random.normal(120, 30, num_global_tracks),
        'danceability': np.random.beta(2, 5, num_global_tracks),
        'valence': np.random.beta(2, 2, num_global_tracks),
        'acousticness': np.random.beta(5, 2, num_global_tracks),
        'instrumentalness': np.random.beta(5, 2, num_global_tracks),
        'speechiness': np.random.beta(2, 5, num_global_tracks),
        'liveness': np.random.beta(2, 5, num_global_tracks),}

    return pd.DataFrame(personal_data), pd.DataFrame(global_data)

def load_sample_data():
    """
    Load existing sample data or create new sample data if not found.
    """
    personal_path = SAMPLE_DATA_DIR / 'personal_tracks.csv'
    global_path = SAMPLE_DATA_DIR / 'global_tracks.csv'

    # Check if sample data files exist
    if personal_path.exists() and global_path.exists():
        # Load existing data
        personal_df = pd.read_csv(personal_path)
        global_df = pd.read_csv(global_path)
        print("Successfully loaded existing sample data. ✅")
    #Create new sample data if files do not exist  
    else:
        personal_df, global_df = create_sample_data()
        SAMPLE_DATA_DIR.mkdir(parents=True, exist_ok=True)
        # Save to CSV files
        personal_df.to_csv(SAMPLE_DATA_DIR / 'personal_tracks.csv', index=False)
        global_df.to_csv(SAMPLE_DATA_DIR / 'global_tracks.csv', index=False)
        print("Created new sample data and saved to CSV files. ✅")
    
    # Return the dataframes
    return personal_df, global_df

#Test the data loader
if __name__ == "__main__":
    personal_df, global_df = load_sample_data()
    print(f"Personal Tracks: {len(personal_df)}")
    print(f"Global Tracks: {len(global_df)}")
    print("\nPersonal data colums:", list(personal_df.columns))
    print("\nFirst few rows of personal data:\n", personal_df.head())

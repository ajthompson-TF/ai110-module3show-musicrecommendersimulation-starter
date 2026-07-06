import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song['genre'] == user_prefs['favorite_genre']:
        score += 3.0
        reasons.append("genre match (+3.0)")

    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_points = round(max(0.0, 1 - abs(song['energy'] - user_prefs['target_energy'])), 2)
    if energy_points > 0:
        score += energy_points
        reasons.append(f"energy close to target (+{energy_points})")

    valence_points = round(max(0.0, 1 - abs(song['valence'] - user_prefs['target_valence'])), 2)
    if valence_points > 0:
        score += valence_points
        reasons.append(f"valence close to target (+{valence_points})")

    dance_points = round(max(0.0, 1 - abs(song['danceability'] - user_prefs['target_danceability'])), 2)
    if dance_points > 0:
        score += dance_points
        reasons.append(f"danceability close to target (+{dance_points})")

    likes_acoustic = user_prefs['likes_acoustic']
    is_acoustic = song['acousticness'] >= 0.5
    if likes_acoustic == is_acoustic:
        score += 0.5
        reasons.append("acousticness preference match (+0.5)")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, ", ".join(reasons)))

    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]

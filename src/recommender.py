import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its audio attributes."""
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
    """Represents a user's music taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Object-oriented music recommendation engine."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k recommended songs for a user profile."""
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short text explanation for why a song was recommended."""
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields to numbers."""
    songs = []
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a similarity score and list of matching reasons for one song."""
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0 points)
    target_genre = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    if target_genre and song["genre"].lower() == target_genre.lower():
        score += 2.0
        reasons.append(f"genre match: {song['genre']} (+2.0)")

    # 2. Mood Match (+1.0 point)
    target_mood = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    if target_mood and song["mood"].lower() == target_mood.lower():
        score += 1.0
        reasons.append(f"mood match: {song['mood']} (+1.0)")

    # 3. Energy Closeness (up to +1.0 point)
    target_energy = user_prefs.get("energy") or user_prefs.get("target_energy")
    if target_energy is not None:
        energy_score = 1.0 - abs(target_energy - song["energy"])
        score += energy_score
        reasons.append(f"energy closeness (+{energy_score:.2f})")

    # 4. Valence Closeness (up to +1.0 point, if provided)
    target_valence = user_prefs.get("valence") or user_prefs.get("target_valence")
    if target_valence is not None:
        valence_score = 1.0 - abs(target_valence - song["valence"])
        score += valence_score
        reasons.append(f"valence closeness (+{valence_score:.2f})")

    # 5. Acousticness Closeness (up to +1.0 point, if provided)
    target_acousticness = user_prefs.get("acousticness") or user_prefs.get("target_acousticness")
    if target_acousticness is not None:
        acoustic_score = 1.0 - abs(target_acousticness - song["acousticness"])
        score += acoustic_score
        reasons.append(f"acousticness closeness (+{acoustic_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs against user preferences and return the top k matches."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "No strong matches"
        scored_songs.append((song, score, explanation))

    # Sort from highest score (item[1]) to lowest score and return the top k
    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]

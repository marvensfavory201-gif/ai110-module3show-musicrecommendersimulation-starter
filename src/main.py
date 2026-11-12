"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # 3 Distinct Standard Profiles + 2 Adversarial Edge Case Profiles
    test_profiles = {
        "1. High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.85},
        "2. Chill Lofi Study": {"genre": "lofi", "mood": "chill", "energy": 0.40},
        "3. Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90},
        "4. Edge Case - Conflicting Vibe": {"genre": "metal", "mood": "sad", "energy": 0.95},
        "5. Edge Case - Unknown Genre": {"genre": "opera", "mood": "peaceful", "energy": 0.20},
    }

    for profile_name, user_prefs in test_profiles.items():
        print("=" * 60)
        print(f"PROFILE: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 60)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} by {song['artist']} (Score: {score:.2f})")
            print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()

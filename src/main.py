"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("=" * 55)
    print("🎵 MUSIC RECOMMENDER SIMULATION")
    print(f"User Profile: {user_prefs}")
    print("=" * 55)
    print("\nTop 5 Recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} by {song['artist']}")
        print(f"   Score:   {score:.2f} / 4.00")
        print(f"   Reasons: {explanation}")
        print("-" * 55)


if __name__ == "__main__":
    main()

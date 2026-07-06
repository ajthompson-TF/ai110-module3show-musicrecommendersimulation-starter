"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    # print(f"Loaded songs: {len(songs)}")

    # Taste profile: target values used by the recommender for comparisons.
    # Kept broad (mid-range energy, acoustic openness) so it doesn't only
    # match a single narrow slice of the catalog.
    taste_profile = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.7,
        "target_valence": 0.75,
        "target_danceability": 0.7,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(taste_profile, songs, k=5)

    print("\n" + "=" * 50)
    print("Top Recommendations")
    print("=" * 50)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} — {song['artist']} (Score: {score:.2f})")
        for reason in explanation.split(", "):
            print(f"   - {reason}")


if __name__ == "__main__":
    main()

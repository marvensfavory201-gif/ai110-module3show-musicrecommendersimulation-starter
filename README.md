# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple music recommender that suggests songs from `songs.csv` based on a user's favorite style and mood. It scores every song by how closely it matches what the listener likes, then picks the top results.

---

## How The System Works

## How The System Works

Real-world apps like Spotify recommend music by looking at both **what other people listen to** and **what the song actually sounds like**. Since this project does not have millions of users, my recommender focuses only on **what the song sounds like** using the attributes in `data/songs.csv`.

### Features Used

* **`Song` Features:**
  * **Basic Info:** `id`, `title`, `artist`
  * **Labels:** `genre` and `mood`
  * **Audio Numbers:** `energy`, `valence` (happiness), `acousticness`, `danceability`, and `tempo_bpm`

* **`UserProfile` Features:**
  * **Favorites:** `favorite_genre` and `favorite_mood`
  * **Target Sound:** `target_energy`, `target_valence`, and `target_acousticness`

### How Songs Are Chosen

1. **Scoring:** Each song gets points out of 100. It gets bonus points if the `mood` (+30) or `genre` (+20) matches. It also gets points based on how close its `energy`, `valence`, and `acousticness` numbers are to the user's preferences.
2. **Ranking:** The system removes songs the user already liked, sorts the rest from highest score to lowest score, and recommends the **Top 3** songs.


### Algorithm Recipe (Scoring & Ranking)

1. **Genre Match (`+2.0` points):** Adds `2.0` points if the song's `genre` matches `favorite_genre`.
2. **Mood Match (`+1.0` point):** Adds `1.0` point if the song's `mood` matches `favorite_mood`.
3. **Sound Similarity (up to `+3.0` points total):** Adds up to `1.0` point each for how close `energy`, `valence`, and `acousticness` are to the user's targets using `1 - abs(target - song_value)`.
4. **Ranking:** Sorts all songs from highest score (`6.0` max) to lowest score and recommends the **Top 3** matches.

### Potential Biases

* **Genre Tunnel Vision:** Because a `genre` match (`+2.0`) is worth twice as much as a `mood` match (`+1.0`), the system might trap the listener in one style and skip great songs in other genres that fit the exact same mood.
* **Small Catalog Bias:** With only 18 songs in `songs.csv`, genres with multiple tracks (like `lofi` or `pop`) have a higher chance of filling the top 3 spots compared to genres with only one track.




---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Top 5 Recommendations:

1. Sunrise City by Neon Echo
   Score:   3.98 / 4.00
   Reasons: genre match: pop (+2.0), mood match: happy (+1.0), energy closeness (+0.98)
-------------------------------------------------------
2. Gym Hero by Max Pulse
   Score:   2.87 / 4.00
   Reasons: genre match: pop (+2.0), energy closeness (+0.87)
-------------------------------------------------------
3. Rooftop Lights by Indigo Parade
   Score:   1.96 / 4.00
   Reasons: mood match: happy (+1.0), energy closeness (+0.96)
-------------------------------------------------------
4. City Hustle by Metro Flow
   Score:   0.95 / 4.00
   Reasons: energy closeness (+0.95)
-------------------------------------------------------
5. Night Drive Loop by Neon Echo
   Score:   0.95 / 4.00
   Reasons: energy closeness (+0.95)
-------------------------------------------------------
```


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this




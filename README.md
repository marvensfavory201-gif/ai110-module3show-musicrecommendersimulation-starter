# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple music recommender that suggests songs from `songs.csv` based on a user's favorite style, mood, and energy level. It scores every song by how closely it matches what the listener likes, then picks the top results.

---

## How The System Works

Real-world apps like Spotify recommend music by looking at both **what other people listen to** and **what the song actually sounds like**. Since this project does not have millions of users, my recommender focuses only on **what the song sounds like** using the attributes in `data/songs.csv`.

### Features Used

* **`Song` Features:**
  * **Basic Info:** `id`, `title`, `artist`
  * **Labels:** `genre` and `mood`
  * **Audio Numbers:** `energy`, `valence` (happiness), `acousticness`, `danceability`, and `tempo_bpm`

* **`UserProfile` Features:**
  * **Favorites:** `genre` and `mood`
  * **Target Sound:** `energy` (plus optional `valence` and `acousticness`)

### Algorithm Recipe (Scoring & Ranking)

1. **Genre Match:** Adds points if the song's `genre` matches the user's favorite genre (`+2.0` initially, later tested at `+1.0`).
2. **Mood Match:** Adds `+1.0` point if the song's `mood` matches the user's favorite mood.
3. **Sound Similarity:** Adds points based on how close `energy` is to the user's target using `1 - abs(target - song_value)` (later doubled to `2.0x` weight).
4. **Ranking:** Sorts all songs from highest score to lowest score and recommends the **Top 5** matches.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

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

---

## Sample Recommendation Output

```text
============================================================
PROFILE: 1. High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85}
============================================================
1. Sunrise City by Neon Echo (Score: 3.97)
   Reasons: genre match: pop (+2.0), mood match: happy (+1.0), energy closeness (+0.97)
2. Gym Hero by Max Pulse (Score: 2.92)
   Reasons: genre match: pop (+2.0), energy closeness (+0.92)
3. Rooftop Lights by Indigo Parade (Score: 1.91)
   Reasons: mood match: happy (+1.0), energy closeness (+0.91)
4. City Hustle by Metro Flow (Score: 1.00)
   Reasons: energy closeness (+1.00)
5. Neon Horizon by Pulsewave (Score: 0.96)
   Reasons: energy closeness (+0.96)

============================================================
PROFILE: 5. Edge Case - Unknown Genre
Preferences: {'genre': 'opera', 'mood': 'peaceful', 'energy': 0.2}
============================================================
1. Moonlight Sonata by Clara Keys (Score: 1.95)
   Reasons: mood match: peaceful (+1.0), energy closeness (+0.95)
2. Spacewalk Thoughts by Orbit Bloom (Score: 0.92)
   Reasons: energy closeness (+0.92)
3. Pine Trail by Willow Creek (Score: 0.88)
   Reasons: energy closeness (+0.88)
4. Library Rain by Paper Lanterns (Score: 0.85)
   Reasons: energy closeness (+0.85)
5. Coffee Shop Stories by Slow Stereo (Score: 0.83)
   Reasons: energy closeness (+0.83)
```

---

## Experiments You Tried

* **Weight Shift (Halving Genre, Doubling Energy):** When `genre` was worth `+2.0` points, the intense workout track *Gym Hero* (`pop`, `intense`) ranked #2 for a **Happy Pop** listener even though its mood did not match. When I cut the `genre` bonus to `+1.0` and doubled the `energy` weight, the recommendations became much better at matching the right vibe across different genres.
* **Diverse & Adversarial User Profiles:** I tested standard listeners (**High-Energy Pop**, **Chill Lofi Study**, **Deep Intense Rock**) alongside edge cases like an **Unknown Genre** (`opera`). Even when `opera` was missing from the catalog, the system safely fell back on mood and low energy to recommend *Moonlight Sonata* (`classical`, `peaceful`).

---

## Limitations and Risks

* **Tiny & Uneven Catalog:** With only 18 songs in `songs.csv`, genres with multiple tracks (like `lofi` and `pop`) fill out top-5 playlists easily, while single-song genres (like `rock` or `classical`) force the system to pad results with unrelated styles.
* **Genre Filter Bubble:** Giving too much weight to exact genre labels can hide great songs from neighboring genres that fit the listener's mood better.
* **Missing Context:** The system does not consider lyrics, language, tempo, or whether the user has already heard a song.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

* **Biggest Learning Moment:** My biggest learning moment was seeing how much a single scoring weight can change the final playlist. When genre was worth twice as much as mood, the system pushed intense workout songs into a "Happy Pop" playlist just because the genre label matched.
* **Working with AI Tools:** Using AI helped me quickly write the CSV loader, test edge cases, and shift my scoring weights. However, I still had to double-check the math and terminal outputs myself, such as making sure the sorting rule ranked by numeric score and verifying that my weight changes kept the total score balanced.
* **What Surprised Me:** I was surprised by how smart a simple math formula can "feel" to a listener. Even with just 18 songs and basic subtraction, the recommender still picked fitting classical music when a user asked for `opera`, a genre not in the catalog.
* **What I Would Try Next:** If I extended this project, I would add a "skip" or "already heard" filter so users never get repeated songs, and I would include `tempo_bpm` and `danceability` in the default score.

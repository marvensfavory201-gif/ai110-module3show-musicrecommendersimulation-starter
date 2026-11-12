# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

This model recommends songs from a small music list based on a listener's favorite genre, mood, and energy level. It assumes users know what style and energy they want right now, and it is built strictly for classroom learning rather than a real music streaming app.

---

## 3. How the Model Works  

The system looks at each song's `genre`, `mood`, and `energy` (plus extra sound numbers like happiness and acousticness if provided) and compares them to what the user likes. A song earns bonus points if its genre or mood matches the user's favorites, plus extra points based on how close its energy number is to the user's target. After scoring every song, the system sorts them from highest to lowest score and picks the top 5 matches. In my experiments, I adjusted the weights so energy counts twice as much and genre counts half as much, which helps keep the right vibe across different genres.

---

## 4. Data  

The catalog (`songs.csv`) contains **18 songs** across **11 genres** (such as `pop`, `lofi`, `rock`, `hip-hop`, `classical`, `country`, `metal`, `reggae`, `r&b`, `electronic`, and `folk`) and several moods (like `happy`, `chill`, `intense`, `peaceful`, and `energetic`). I added 8 new songs to the original 10-song starter file to include more variety. Even with 18 tracks, many styles—like Latin, K-pop, and world music—are still missing, and most genres only have one song.

---

## 5. Strengths  

* **Clear Vibe Matching:** Works well for listeners with clear goals, such as finding calm `lofi` tracks for studying or upbeat `pop` tracks for working out.
* **Smart Fallback:** Even when a user asks for a genre not in the catalog (like `opera`), the model still recommends fitting songs by relying on mood and energy closeness.
* **Easy to Understand:** Every recommendation comes with plain-text reasons showing exact points earned for genre, mood, and energy.

---

## 6. Limitations and Bias 

During my experiments, I discovered that the system creates a "filter bubble" when genre is weighted twice as heavily as mood, trapping users inside one genre label even when other genres fit their vibe better. Additionally, the 18-song catalog is uneven because genres like `lofi` (3 songs) and `pop` (2 songs) appear multiple times, while genres like `jazz`, `rock`, and `classical` only appear once. As a result, users who like single-song genres quickly get pushed into unrelated styles to fill out their top 5 list. Finally, the model ignores lyrics, language, and artist variety, which can make playlists feel repetitive.

---

## 7. Evaluation  

I tested five different listener profiles in `src/main.py` to see if the top 5 recommendations made sense:

* **Profiles Tested:**
  1. **High-Energy Pop** (`pop`, `happy`, energy `0.85`)
  2. **Chill Lofi Study** (`lofi`, `chill`, energy `0.40`)
  3. **Deep Intense Rock** (`rock`, `intense`, energy `0.90`)
  4. **Edge Case – Conflicting Vibe** (`metal`, `sad`, energy `0.95`)
  5. **Edge Case – Unknown Genre** (`opera`, `peaceful`, energy `0.20`)

* **What Surprised Me:**
  At first, the workout song *Gym Hero* kept showing up near the top for **Happy Pop** even though its mood is `intense`, not `happy`. This happened because matching the `pop` genre gave it a huge bonus that hid its wrong mood. When I cut the genre bonus in half and doubled the energy score, the playlist became much better at matching the right mood across different genres.

* **Profile Comparisons:**
  * **High-Energy Pop vs. Chill Lofi Study:** High-Energy Pop picks fast, upbeat songs like *Sunrise City* (energy `0.82`), while Chill Lofi shifts completely to calm study tracks like *Midnight Coding* (energy `0.42`). This makes sense because their energy and mood targets are total opposites.
  * **Deep Intense Rock vs. Unknown Genre (Opera):** Deep Intense Rock puts loud tracks like *Storm Runner* (energy `0.91`) at #1. When the Opera profile asks for a genre that is not in the catalog, the system safely falls back on mood and low energy, picking *Moonlight Sonata* (`classical`, `peaceful`, energy `0.15`) first.

---

## 8. Future Work  

* **Add a "Skip" or "Already Played" Filter:** Prevent the recommender from suggesting songs the user has already heard or disliked.
* **Limit Repeated Artists:** Add a rule so the same artist cannot take over multiple spots in the top 5 list.
* **Use More Audio Features:** Always include `tempo_bpm`, `danceability`, and `acousticness` in the default score so slow ballads and fast dance songs are easier to tell apart.

---

## 9. Personal Reflection  

* **Biggest Learning Moment:** My biggest learning moment was seeing how much a single scoring weight can change the final playlist. When genre was worth twice as much as mood, the system pushed intense workout songs into a "Happy Pop" playlist just because the genre label matched.
* **Working with AI Tools:** Using AI helped me quickly write the CSV loader, test edge cases, and shift my scoring weights. However, I still had to double-check the math and terminal outputs myself—for example, making sure the sorting rule ranked by score instead of song dictionary keys and verifying that my weight changes kept the total score balanced.
* **What Surprised Me:** I was surprised by how smart a simple math formula can "feel" to a listener. Even with just 18 songs and basic subtraction (`1 - abs(target - energy)`), the recommender still picked fitting classical music when a user asked for `opera`, a genre that was not even in the file.
* **What I Would Try Next:** If I extended this project, I would add a "skip" or "already heard" filter so users never get repeated songs, and I would include `tempo_bpm` and `danceability` in the default score to make the mood matching even sharper.


# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

`Song` will have features such as genre, mood, energy, and tempo. The `UserProfile` may keep track of a user's preferred genre, mood, energy, and tempo values. A `Recommender` will calculate which songs are closest to a user's preference based on the difference between the respective values, matches, and recommend the most appropiate songs using a point-based system. Matches for genre will weigh the most; therefore, this system might over-prioritize genre, ignoring great songs that match the user's mood.

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

```
==================================================
Top Recommendations
==================================================

1. Sunrise City — Neon Echo (Score: 7.70)
   - genre match (+3.0)
   - mood match (+1.5)
   - energy close to target (+0.88)
   - valence close to target (+0.91)
   - danceability close to target (+0.91)
   - acousticness preference match (+0.5)

2. Gym Hero — Max Pulse (Score: 6.07)
   - genre match (+3.0)
   - energy close to target (+0.77)
   - valence close to target (+0.98)
   - danceability close to target (+0.82)
   - acousticness preference match (+0.5)

3. Rooftop Lights — Indigo Parade (Score: 4.76)
   - mood match (+1.5)
   - energy close to target (+0.94)
   - valence close to target (+0.94)
   - danceability close to target (+0.88)
   - acousticness preference match (+0.5)

4. Golden Horizon — Marcus Vale (Score: 3.24)
   - energy close to target (+0.9)
   - valence close to target (+0.99)
   - danceability close to target (+0.85)
   - acousticness preference match (+0.5)

5. Island Sway — Sunny Tide (Score: 3.20)
   - energy close to target (+0.75)
   - valence close to target (+0.95)
   - danceability close to target (+1.0)
   - acousticness preference match (+0.5) 
   ```

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




# 🧩 Puzzle Hero

An interactive web app for teaching combinations and permutations to Mathayom 1–3 students.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://puzzle-hero.streamlit.app)

---

## 📘 About

Puzzle Hero helps students practice logical math thinking by solving character-based code puzzles.

Students calculate how many valid combinations exist based on certain rules, and enter their answers to progress through levels.

---

## 🎓 Educational Use

- Designed for Thai Mathayom 1–3 students
- Aligns with combinatorics and basic probability lessons
- Great for classroom or self-paced learning

---

## 🧠 How It Works

1. The app presents a code puzzle (e.g., 4 characters, no repeats).
2. Students determine the number of possible combinations.
3. They input their multiplication steps (e.g., `36 × 35 × 34 × 33`).
4. If correct, they earn points and level up!

---

## 📊 Ranks & Scoring

| Score       | Rank              |
|-------------|-------------------|
| 0–4         | 🐣 Novice Cipherer |
| 5–9         | 🔓 Puzzle Adept    |
| 10          | 🧠 Master of Numbers |

---

## 📝 Use with Worksheet

A printable worksheet is available for offline solving.  
Students solve by hand first, then check their answers in the app.

---

## 🚀 Getting Started

1. Make sure you have Python 3.7+ installed.
2. Install required packages:

    ```bash
    pip install streamlit qrcode pillow
    ```

3. Save the script (e.g., `streamlit-app.py`).
4. Place level images (`level0.webp`, `level1.webp`, `level2.webp`) and number of characters images (`3char.png`, `4char.png`, `5char.png`) in the same directory.
5. Run the app:

    ```bash
    streamlit run streamlit-app.py
    ```

---

## File Structure
```plaintext
/puzzle-hero
├── streamlit-app.py     # Main Streamlit app script
├── level0.webp          # Novice Cipherer rank image
├── level1.webp          # Puzzle Adept rank image
├── level2.webp          # Master of Numbers rank image
├── 3char.png            # Image representing 3-character codes
├── 4char.png            # Image representing 4-character codes
└── 5char.png            # Image representing 5-character codes
```
---

## Future Improvements

- Improve UI with animations and progress bars.
- Allow users to track historical performance and stats.

---

## License

MIT License – free to use for teachers and students.

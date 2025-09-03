# Puzzle-Hero

Puzzle-Hero is an interactive Streamlit web app that challenges users to solve combination problems involving characters (letters and numbers). Users solve multiplication step problems to advance through ranks, earn points, and ultimately become a "Master of Numbers."

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://puzzle-hero.streamlit.app/)

---

## Features

- Generates random combination problems with varying character types (lowercase, uppercase, numbers)
- Supports problems where characters can or cannot repeat
- Displays a QR code to open the app easily on mobile devices
- Tracks user score and assigns ranks based on performance
- Displays rank badges with level images
- Shows detailed feedback with correct answers on incorrect attempts
- Enables replay and restart functionality after game completion

---

## How to Use

1. Open the app (or scan the QR code in the sidebar to open it on your mobile).
2. Read the problem description and restrictions for the code.
3. Enter the multiplication steps representing the number of valid codes (e.g., `62 × 61 × 60`).
4. Submit your answer.
5. If correct, proceed to the next problem and increase your score.
6. Reach a score of 10 to become a "Master of Numbers" and complete the game.
7. Restart anytime after completion or try new problems as you wish.

---

## Technical Details

### Problem Generation

- Randomly selects character types from lowercase letters, uppercase letters, and numbers.
- Randomly decides if characters can repeat in the code or not.
- Generates code lengths between 3 and 5 characters.
- Calculates the total number of possible characters based on selected types.
- Forms multiplication formulas representing the total number of valid combinations.

### Scoring and Ranking

- Score starts at 0.
- Ranks are assigned based on score:
  - 0–4: Novice Cipherer
  - 5–9: Puzzle Adept
  - 10: Master of Numbers
- Displays rank image and score in the main app interface.

### User Interface

- Uses Streamlit for an interactive UI.
- Displays rank and score with relevant images.
- Sidebar contains a QR code linking to the app.
- Input form for users to submit their answers.
- Provides immediate feedback with success or error messages.
- Shows the correct formula on incorrect attempts.

---

## Installation

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

This project is open-source and available under the MIT License.

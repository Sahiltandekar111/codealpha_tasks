# Hangman Game 🎮

A simple **text-based Hangman game** built in Python.  
The player guesses a word one letter at a time, with a limited number of attempts.

---

## Features
- Predefined list of words (`relience`, `chemistry`, `aeroplane`, `helicopter`, `doctor`)
- Random word selection using `random.choice()`
- 6 incorrect attempts allowed
- Displays progress with underscores `_` for unguessed letters
- Validates user input (only single alphabet letters allowed)
- Ends with either **win** or **game over**

---

## How to Run
1. Make sure you have Python installed (Python 3 recommended).
2. Save the script as `hangman.py`.
3. Run the game in your terminal:
   ```bash
   python hangman.py

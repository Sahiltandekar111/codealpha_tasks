import random

words = ["relience", "chemistry", "aeroplane", "helicopter", "doctor"]

guess_letter = []

# Randomly choose a word from the list
word = random.choice(words)

attempt = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Game loop runs until attempts run out
while attempt > 0:
    # Display current progress of the word
    display_word = ""
    for letter in word:
        if letter in guess_letter:
            display_word += letter  
        else:
            display_word += "_ "    
    print("\nWord:", display_word.strip())

    # Check if all letters are guessed
    if all(letter in guess_letter for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break


    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guess_letter:
        print("You already guessed that letter.")
    elif guess in word:
        print("✅ Correct guess!")
        guess_letter.append(guess)
    else:
        print("❌ Wrong guess!")
        attempt -= 1
        guess_letter.append(guess)
        print("Remaining attempts:", attempt)

# End of game
if attempt == 0:
    print("💀 Game Over! The word was:", word)


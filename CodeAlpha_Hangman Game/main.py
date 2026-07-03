import random

words = ["relience","chemistry","aeroplane","helicopter","doctor"]

guess_letter =[]

word = random.choice(words)

attempt = 6

print("welcome to hangman game!")
print("Guess the word, one letter at a time")


while attempt > 0:
    display_word = ""
    for letter in word:
        if letter in guess_letter:
            display_word += letter
        else:
            display_word += "_ "
    print("\nword",display_word.strip())

    if all(letter in guess_letter for letter in word):
        print("Congradulation you guess the word",word)
        break


    guess = input("Enter a letter").lower()
    if len(guess) != 1 or not guess.isalpha:
        print("please enter single letter")
    if guess in guess_letter:
        print("you aleady guess the letter")
    elif guess in word:
        print("Correct guess")
        guess_letter.append(guess)
    else:
        print("Wrong letter")
        attempt -= 1
        guess_letter.append(guess)
        
        print("Remaining attempt",attempt)
if attempt == 0:
    print("game over")

        
    

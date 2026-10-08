
                       ## HANGMAN GAME

import random

words = ["python", "intern", "script", "coding", "developer"]
word = random.choice(words)

guesses = []
wrong_count = 0

print("Welcome to Hangman!")

while wrong_count < 6:
    current_word = ""
    
    for char in word:
        if char in guesses:
            current_word += char
        else:
            current_word += "_"
            
    print("\nWord:", current_word)
    
    if "_" not in current_word:
        print("You win! The word was", word)
        break
        
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1:
        print("Please enter exactly one letter.")
        continue
        
    if guess in guesses:
        print("You already guessed that letter.")
        continue
        
    guesses.append(guess)
    
    if guess not in word:
        wrong_count += 1
        print("Incorrect guess. Chances left:", 6 - wrong_count)
    else:
        print("Correct guess!")

if wrong_count == 6:
    print("Game Over. The word was", word)

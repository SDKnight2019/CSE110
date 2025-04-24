import random

def generate_hint(secret_word, guess):
    """Generates a hint based on the guess compared to the secret word."""
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # Correct letter, correct position
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  # Correct letter, wrong position
        else:
            hint.append("_")  # Letter not in the word
    return "".join(hint)

def word_guessing_game():
    """Main function to run the word guessing game."""
    words = ["temple", "moroni", "mosiah", "zion", "nephi"]  # List of possible words
    secret_word = random.choice(words)  # Select a random word
    guess_count = 0
    
    print("Welcome to the word guessing game!")
    
    while True:
        guess = input("What is your guess? ").lower()
        
        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long.")
            continue
        
        guess_count += 1
        
        if guess == secret_word:
            print("Congratulations! You guessed it!")
            print(f"It took you {guess_count} guesses.")
            break
        else:
            print("Your guess was not correct.")
            print("Hint:", generate_hint(secret_word, guess))

if __name__ == "__main__":
    word_guessing_game()
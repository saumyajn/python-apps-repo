import requests
import random
from hangman_art import logo, stages

print(logo)


# Function to get random 100 words
def get_word_list():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=100")
    if response.status_code == 200:
        return response.json()  # Returns a Python list of strings
    return []


print("Welcome!\nA word has been randomly generated. Lets play!!")


def play_game():
    lives = 6
    word_list = get_word_list()
    if not word_list:
        print("Could not fetch words. Exiting.")
        return
    random_word = random.choice(word_list)
    word_len = len(random_word)
    print(stages[0])

    placeholder = "_" * word_len

    print("Word to guess: " + placeholder)

    game_over = False
    guessed = []
    correct_letters = []
    while not game_over:
        guess = input("Guess a letter: ").lower()
        while guess in guessed:
            print(
                f"Oops! You already guessed the letter '{guess}' before. Please guess a new letter!"
            )
            guess = input("Guess a letter: ").lower()
        guessed.append(guess)
        display = ""
        for letter in random_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(f"Word to Guess: {display}\n")
        if guess not in random_word:
            print(stages[-lives])
            lives -= 1
            print(
                f"You guessed '{guess}', that is not in the word. You lost a life!! 💀\n"
            )
            if lives == 0:
                game_over = True
                print("**** YOU LOSE ****")
                print(f"The correct word was - '{random_word}'")

        if "_" not in display:
            game_over = True
            print("**** YOU WON ****")
            print("You guessed the correct word.")


if __name__ == "__main__":
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").strip().lower()
        while again not in ("y", "n", "yes", "no"):
            again = input("Please enter 'y' or 'n': ").strip().lower()
        if again in ("n", "no"):
            print("Thanks for playing! Goodbye.")
            break

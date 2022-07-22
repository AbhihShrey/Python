import random
import string

words = ["hangman", "python", "happy", "mississippi"]


def check_win(used_letters, word):
    print(used_letters, word)

    used_letter_set = set(used_letters)
    word_set = set(word)

    print(used_letter_set, word_set)

    if used_letter_set == word_set:
        return True
    return False


def hangman():
    word = random.choice(words)
    word_letters = set(word)  # Getting the letters in the word
    # Creating all the letters than can be used, making uppercase so it is easier
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Creating an empty set for used letters
    attempts = 15

    # Play the game till you win or run out of attempts
    win = False
    while attempts != 0 or win == False:

        # Making it upper because it is easier
        prompt = f"Tries remaining {attempts}. Guess a letter: "
        user_letter = input(prompt)
        used_letters.add(user_letter)
        attempts = attempts - 1

        # Print the used letters
        print(f"You have used these letters: {used_letters}")

        # Replace ---- with the correct letters in word
        partial_word = [
            letter if letter in used_letters else '-' for letter in word]
        print(f"Current solved word {partial_word}")

        # Check if the word is complete. Otherwise continue to ask another letter
        win = check_win(used_letters, word)

    if win:
        print("WIN")
    else:
        print("LOSE")


hangman()

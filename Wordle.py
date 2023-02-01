import pathlib, random
from string import ascii_letters


def get_random_word():
    """Choose a random word from the wordist that has been generated"""

    # acquire the list of words
    wordlist = pathlib.Path("wordlist.txt")

    # sort the file and grab each word on a new line and then choose a random word
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def show_guess(guess, word):
    """Compare the users inputted word to the randomly chosen word"""

    # check each letter and if it's the right letter and in correct spot,
    # put into a list
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }

    # put letters that are correct put not in the correct position into a list
    misplaced_letters = set(guess) & set(word) - correct_letters

    # state the letters that are not in the word at all into a list
    wrong_letters = set(guess) - set(word)

    # Show the user the information about their guess
    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Incorrect letters:", ", ".join(sorted(wrong_letters)))


def game_over(word):
    """Display what the word the user was trying to guess"""

    print(f"The word was {word}")



def main():
    # This will start the pre-process of the game of getting a word
    word = get_random_word()

    #This will be the main process of the game of actually playing
    for guess_number in range(1, 7):
        guess = input(f"Guess {guess_number}: ").upper()

        show_guess(guess, word)
        if guess == word:
            break


    # This will the post process of the game, displaying the result
    else:
        game_over(word)


if __name__ == "__main__":
    main()
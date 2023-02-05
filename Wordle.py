import pathlib, random
from string import ascii_letters, ascii_uppercase
from rich.console import Console
from rich.theme import Theme
import contextlib

CONSOLE = Console(width=50, theme=Theme({"warning": "red on yellow"}))

NUM_OF_LETTERS = 5
NUM_OF_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / "wordlist.txt"


def guess_word(previous_guesses):

    guess = CONSOLE.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        CONSOLE.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)

    if len(guess) != NUM_OF_LETTERS:
        CONSOLE.print(f"Your guess must be {NUM_OF_LETTERS} letters", style="warning")
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        CONSOLE.print(
            f"Invalid letter: '{invalid}'. You must use English letters.",
            style="warning",
        )
        return guess_word(previous_guesses)

    return guess



def get_random_word(word_list):
    """Choose a random word from the wordist that has been generated
    
    ##Example:
    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """

    # sort the file and grab each word on a new line and then choose a random word
    if words := [
        word.upper()
        for word in word_list
        if len(word) == NUM_OF_LETTERS and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        CONSOLE.print(f"No words of length {NUM_OF_LETTERS} in the word list", style="warning")
        raise SystemExit()


def clear_page(headline):
    """Clears the page, and allows for a clearer display"""

    CONSOLE.clear()
    CONSOLE.rule(f"[bold blue]:rose: {headline} :rose:[/]\n")


def show_guesses(guesses, word):
    """Compare the users inputted word to the randomly chosen word

    ## Example:
    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Incorrect letters: C, R
    """

    # Stylise each guess depending on the letters used
    status_of_letters = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        stylised_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            stylised_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                status_of_letters[letter] = f"[{style}]{letter}[/]"
                

        CONSOLE.print("".join(stylised_guess), justify="center")
    CONSOLE.print("\n" + "".join(status_of_letters.values()), justify="center")


def game_over(guesses, word, correctly_guessed):
    """Display what the word the user was trying to guess"""

    clear_page(headline="Game Over")
    show_guesses(guesses, word)

    # State whether the used was right on their last go
    if correctly_guessed:
        CONSOLE.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        CONSOLE.print(f"\n[bold white on red]Sorry, the word was {word}[/]")


def main():
    # This will start the pre-process of the game of getting a word
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(WORDS_PATH.read_text(encoding="utf-8"). split("\n"))
    total_guesses = ["_" * NUM_OF_LETTERS] * NUM_OF_GUESSES

    print(word)

    #This will be the main process of the game of actually playing
    with contextlib.suppress(KeyboardInterrupt):
        for index in range(NUM_OF_GUESSES):
            clear_page(headline=f"Guess {index + 1}")
            show_guesses(total_guesses, word)

            total_guesses[index] = guess_word(previous_guesses=total_guesses[:index])
            if total_guesses[index] == word:
                break

    # This will the post process of the game, displaying the result
    game_over(total_guesses, word, correctly_guessed=total_guesses[index] == word)


if __name__ == "__main__":
    main()
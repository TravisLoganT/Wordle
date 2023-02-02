import pathlib, random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

CONSOLE = Console(width=40, theme=Theme({"warning": "red on yellow"}))


def get_random_word(word_list):
    """Choose a random word from the wordist that has been generated
    
    ##Example:
    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """

    # sort the file and grab each word on a new line and then choose a random word
    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


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

        CONSOLE.print("".join(stylised_guess), justify="center")


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
    word = get_random_word(words_path.read_text(encoding="utf-8"). split("\n"))
    total_guesses = ["_" * 5] * 6

    print(word)

    #This will be the main process of the game of actually playing
    for index in range(6):
        clear_page(headline=f"Guess {index + 1}")
        show_guesses(total_guesses, word)

        total_guesses[index] = input("\nGuess word: ").upper()
        if total_guesses[index] == word:
            break

    # This will the post process of the game, displaying the result
    game_over(total_guesses, word, correctly_guessed=total_guesses[index] == word)


if __name__ == "__main__":
    main()
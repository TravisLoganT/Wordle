WORD = "BLACK"

for guess_number in range(1, 7):
    # Get a chosen word from the user
    guess = input(f"Guess {guess_number}: ").upper() 

    # Display if the user has successfully guessed the word
    if guess == WORD:
        print("Correct")
        break
    
    # check each letter and if it's the right letter and in correct spot,
    # put into a list
    correct_letters = {
        letter for letter, correct in zip(guess, WORD) if letter == correct
    }

    # put letters that are correct put not in the correct position into a list
    misplaced_letters = set(guess) & set(WORD) - correct_letters

    # state the letters that are not in the word at all into a list
    wrong_letters = set(guess) - set(WORD)

    # Show the user the information about their guess
    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Incorrect letters:", ", ".join(sorted(wrong_letters)))


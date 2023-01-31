for guess_number in range(1, 7):
    # Get a chosen word from the user
    guess = input(f"Guess {guess_number}: ").upper() 

    # Display if the user has successfully guessed the word
    if guess == "PEPSI":
        print("Correct")
        break
    
    print("Wrong")
# Import the random module to generate random numbers.
import random

# Define the main function for the number guessing game.
def start_number_guess_game():
    # Generate a random number between 1 and 100 for the player to guess.
    target_value = random.randint(1, 100)
    
    # Initialize a counter to track the number of attempts made by the player.
    attempt_counter = 0

    # Display a welcome message and explain the rules of the game.
    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    
    # Start a loop to keep the game running until the player guesses correctly or quits.
    while True:
        # Prompt the player for a guess or to quit the game.
        user_guess = input("Enter your guess (or type 'quit' to exit): ")
        
        # Check if the player wants to quit by typing 'quit'.
        if user_guess.lower() == 'quit':
            # Inform the player of the correct answer and exit the loop.
            print("Thanks for playing! The number was:", target_value)
            break
        
        # Validate if the input is a number. If not, prompt again.
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue  # Skip the rest of the loop and ask again.
        
        # Convert the valid input string into an integer for comparison.
        user_guess = int(user_guess)
        
        # Increment the attempt counter for every valid guess.
        attempt_counter += 1
        
        # Check if the player's guess matches the target value.
        if user_guess == target_value:
            # Congratulate the player and display the number of attempts made.
            print(f"Congratulations! You've guessed the number in {attempt_counter} attempts.")
            break  # Exit the loop since the game is over.
        elif user_guess < target_value:
            # Inform the player if their guess is too low.
            print("Too low! Try again.")
        else:
            # Inform the player if their guess is too high.
            print("Too high! Try again.")

# Call the function to start the game when the script is run.
start_number_guess_game()

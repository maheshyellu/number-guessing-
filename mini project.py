import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print(" Too low. Try again.")
        elif guess > number_to_guess:
            print(" Too high. Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print(" Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

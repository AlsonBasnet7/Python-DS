import random

def play_game():
    print("Welcome to the Number Guessing Game!")

    while True:
        print("\nSelect Difficulty Level:")
        print("1. Easy (1–10)")
        print("2. Medium (1–50)")
        print("3. Hard (1–100)")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            max_num = 10
        elif choice == "2":
            max_num = 50
        elif choice == "3":
            max_num = 100
        else:
            print("Invalid choice! Try again.")
            continue

        number = random.randint(1, max_num)
        attempts = 0

        print(f"\nI have selected a number between 1 and {max_num}.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    break

            except ValueError:
                print("Please enter a valid number!")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break


# Run the game
play_game()
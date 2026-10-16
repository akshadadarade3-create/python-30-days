"""Refactor your Day 5 number-guessing game into functions """
import random

def guess():
    
  while True:
    try:
        guess = int(input("guess the number between 1 to 100:"))

        if 1<= guess <=100:
            return guess
        print("Please enter a number between 1 to 100")

    except ValueError:
        print("Invalid input , please enter a valid number ")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI am thinking of a number between 1 and 100.")

    while True:
        player_guess = guess()
        attempts += 1

        if player_guess < secret_number:
            print("Lower !Try again")
        elif player_guess > secret_number:
            print("Higher !Try again")
        else:
            print("You Did it")
            print("Number of attempts:", attempts)
            break

def play_again():
    """Ask the player whether they want another round."""
    while True:
        answer = input("Do you want to play again? (yes/no): ").lower().strip()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter yes or no.")

def main():
    """Run the number-guessing game until the player exits."""
    print("GUESSING GAME")

    while True:
        play_game()

        if not play_again():
            print("Thank You !!!!")
            break
if __name__ == "__main__":
    main()



      


            
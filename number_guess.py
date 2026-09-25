import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess > secret_number:
        print("high")

    elif guess < secret_number:
        print("low")

    else:
        print("Correct!")
        print("Attempts:", attempts)
        break
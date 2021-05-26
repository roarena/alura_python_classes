import random

random.seed()

print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = random.randrange(1, 101)
points = 1000

print("Select the difficulty:\n(1) Easy (2) Normal (3) Hard")
difficulty = int(input("Enter difficulty:"))

if (difficulty == 1):
    round_total = 20
elif (difficulty == 2):
    round_total = 10
else:
    round_total = 5

for current_round in range(1, round_total + 1):
    print(f"Round {current_round} of {round_total}")
    user_input = int(input("Enter a number between 1 and 100: "))

    if (user_input < 1 or user_input > 100):
        print("You should enter a number between 1 and 100.")
        continue

    correct_guess = user_input == secret_number
    higher_guess = user_input > secret_number
    lower_guess = user_input < secret_number

    if (correct_guess):
        print("Congratulations! You guessed correctly.")
        print(f"You got {points} points")
        break
    else:
        if (higher_guess):
            print("Ooops! You guessed a higher number then the secret one.")
        else:
            print("Ooops! You guessed a lower number then the secret one.")

        if(current_round == round_total):
            points = points - abs(secret_number - user_input)

print(f"The secret number was {secret_number}")
print(f"You got {points} points.")

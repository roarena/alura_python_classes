print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 13
round_total = 3

for current_round in range(1, round_total +1):
    print(f"Round {current_round} of {round_total}")
    user_input = int(input("Enter a number between 1 and 100: "))

    if(user_input < 1 or user_input > 100):
        print("You should enter a number between 1 and 100.")
        continue

    correct_guess = user_input == secret_number
    higher_guess = user_input > secret_number
    lower_guess = user_input < secret_number

    if(correct_guess):
        print("Congratulations! You guessed correctly.")
        break
    else:
        if(higher_guess):
            print("Ooops! You guessed a higher number then the secret one.")
        else:
            print("Ooops! You guessed a lower number then the secret one.")

print("The end")



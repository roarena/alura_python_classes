print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 666

user_input = int(input("Enter a number: "))

correct_guess = user_input == secret_number
higher_guess = user_input > secret_number
lower_guess = user_input < secret_number

if(correct_guess):
    print("Congratulations! You guessed correctly.")
else:
    if(higher_guess):
        print("Ooops! You guessed a higher number then the secret one.")
    else:
        print("Ooops! You guessed a lower number then the secret one.")

print("The end")



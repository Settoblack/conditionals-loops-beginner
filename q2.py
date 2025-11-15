# Set the secret number
secret_number = 7

# Ask the user to guess until they get it right
guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong, try again.")
    guess = int(input("Guess the number: "))

print("Correct!")
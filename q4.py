# Set the correct password
correct_password = "python123"

# Prompt the user until they enter the correct password
password = input("Enter password: ")

while password != correct_password:
    print("Wrong password, try again.")
    password = input("Enter password: ")

print("Password accepted!")
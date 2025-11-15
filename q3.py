# Ask the user for a score
score = int(input("Enter score (0–100): "))

# Determine the grade
if 70 <= score <= 100:
    print("A")
elif 60 <= score <= 69:
    print("B")
elif 50 <= score <= 59:
    print("C")
elif 40 <= score <= 49:
    print("D")
elif 0 <= score <= 39:
    print("F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")
# Prompt user to enter a score
score = int(input("Enter the score (0-100): "))

if score > 100:
    grade = "N/A"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade for score {score} is {grade}")

# input validation

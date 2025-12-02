import json
import time

# Load questions from json file
with open("questions.json", "r") as file:
    questions = json.load(file)

print("\n-- Welcome to Quiz App --")
print("You will get 10 points for every correct answer.\n")

score = 0

for q in questions:
    print("--> " + q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"   {i}. {option}")

    # Taking user input
    answer = int(input("Enter your answer (1-4): "))

    # Checking answer
    if answer == q["answer"]:
        print(" Correct!\n")
        score += 10
    else:
        print(" Wrong!")
        correct_option = q["options"][q["answer"] - 1]
        print("Correct answer:", correct_option, "\n")

    time.sleep(0.5)  # Delay for better flow

print(" Quiz Completed!")
print(f"Your Final Score: {score}/{len(questions) * 10}")

if score == len(questions) * 10:
    print(" Excellent! You got all answers correct!")
elif score >= (len(questions) * 7):
    print(" Good job! Keep it up!")
else:
    print(" Keep practicing, you will improve!")

print("\n Thanks for playing!")

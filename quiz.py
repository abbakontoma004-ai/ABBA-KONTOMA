# Step 1: Setup – list of dictionaries
questions = [
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->"],
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a valid Python variable name?",
        "options": ["A. 2name", "B. my-name", "C. my_name"],
        "correct_answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. show()"],
        "correct_answer": "B"
    }
]

score = 0

# Step 2–4: Execute, Interact & Evaluate
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A, B, or C): ").upper()

    if answer == q["correct_answer"]:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

# Step 5: Output – function for percentage and pass/fail
def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(questions))

print("\nQuiz Finished!")
print(f"Your Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("Result: PASS 🎉")
else:
    print("Result: FAIL ❌")
# Step 1: Setup - Create list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "correct_answer": "B"
    },
    {
        "question": "Which data type is used to store multiple items in one variable?",
        "options": ["A. int", "B. float", "C. list", "D. string"],
        "correct_answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit",
                    "B. Computer Personal Unit",
                    "C. Central Power Unit",
                    "D. Control Processing Unit"],
        "correct_answer": "A"
    }
]

# Function to calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100


# Step 2–4: Execute, Interact, Evaluate
score = 0

for question in quiz_questions:
    print("\n" + question["question"])
    
    for option in question["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, D): ").upper()

    if user_answer == question["correct_answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is {question['correct_answer']}")

# Step 5: Output result
total_questions = len(quiz_questions)
percentage = calculate_percentage(score, total_questions)

print("\n----- QUIZ RESULT -----")
print(f"Your Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("Status: PASS ✅")
else:
    print("Status: FAIL ❌")
# ABBAS MUHAMMAD YUSUF
# MAAUN/24/CSC/0052

quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "correct_answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "correct_answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "correct_answer": "B"
    }
]

# Function to calculate percentage
def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100

# 2. Execute: Loop through the quiz
score = 0

for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    # 3. Interact: Get user input
    answer = input("Enter your answer (A, B, C, or D): ").upper()

    # 4. Evaluate: Check answer
    if answer == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", q["correct_answer"])

# 5. Output: Final result
percentage = calculate_percentage(score, len(quiz))
print("\nYour score:", score, "/", len(quiz))
print("Your percentage:", percentage, "%")

if percentage >= 50:
    print("PASS 🎉")
else:
    print("FAIL ❌")
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Computer Personal Unit",
            "C. Central Processing Unit",
            "D. Central Power Unit"
        ],
        "answer": "C"
    }
]questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "correct_answer": "C"
    },
    def calculate_result(score, total_questions):
    percentage = (score / total_questions) * 100
    
    print("\n Quiz Complete!")
    print(f"You scored {score} out of {total_questions}.")
    print(f"Your final percentage is {percentage:.2f}%.")

    if percentage >= 60:
        print(" Great job! You passed! Keep up the good work!")
    else:
        print(" Don't worry! Keep practicing and you'll improve!")


# Welcome message
print("===================================")
print(" Welcome to the CLI Quiz Challenge!")
print("Answer by typing A, B, C, or D.")
print("Let's begin!\n")

score = 0

# 2. Execute: loop through questions
for index, q in enumerate(questions, start=1):
    print(f"\nQuestion {index}: {q['question']}")
    
    for option in q["options"]:
        print(option)
    
    # 3. Interact
    user_answer = input("Your answer: ").strip().upper()
    
    # 4. Evaluate
    if user_answer == q["correct_answer"]:
        print(" Correct! Nice one!")
        score += 1
    else:
        print(f" Oops! The correct answer was {q['correct_answer']}.")

# 5. Output
calculate_result(score, len(questions))
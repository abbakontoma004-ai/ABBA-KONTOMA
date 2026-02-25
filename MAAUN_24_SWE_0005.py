quiz_questions = [
    {
        "question": "Which year did Nigeria get independence?",
        "options": ["A. 1940", "B. 1950", "C. 1960", "D. 1970"],
        "correct_answer": "C"
    },
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Kano", "B. Abuja", "C. Lagos", "D. Kaduna"],
        "correct_answer": "B"
    },
    {
        "question": "Who is the current President of Nigeria?",
        "options": ["A. Bola Ahmed Tinubu", "B. Goodluck Jonathan", "C. Olusegun Obasanjo", "D. Muhammadu Buhari"],
        "correct_answer": "A"
    }
]

def calculate_score(score, total_questions):
    """Calculate the final percentage score"""
    percentage = (score / total_questions) * 100
    return percentage

def evaluate_answer(user_answer, correct_answer):
    """Check if the user's answer is correct"""
    return user_answer.upper() == correct_answer

def run_quiz(questions):
    """Run the quiz and return the final score"""
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ")
        if evaluate_answer(user_answer, question["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['correct_answer']}")

    return score, total_questions

def main():
    score, total_questions = run_quiz(quiz_questions)
    percentage = calculate_score(score, total_questions)
    print(f"\nQuiz complete! Your final score is {score}/{total_questions} ({percentage:.2f}%)")
    if percentage >= 50:
        print("You passed!")
    else:
        print("You failed. Better luck next time!")

if __name__ == "__main__":
    main()
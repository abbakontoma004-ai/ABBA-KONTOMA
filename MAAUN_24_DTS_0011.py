quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
        "correct_answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 11", "B. 12", "C. 13", "D. 14"],
        "correct_answer": "B"
    }
]


def run_cbt(candidate_name):
    total_score = 0
    total_questions = len(quiz_questions)
    
    
    for i, question in enumerate(quiz_questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        
        for option in question['options']:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper().strip()
        
        #check if the answer is correct
        if user_answer == question['correct_answer']:
            print("Correct!")
            total_score += 1
        else:
            print(f"Incorrect. The correct answer was {question['correct_answer']}")
    
    # Calculate percentage and print result
    print("EXAM COMPLETED!")
    print(f"Your Score: {total_score}/{total_questions}")
    
    
    def calculate_percentage(score, max_score):
        """Calculates the percentage and returns it."""
        return (score / max_score) * 100
    
    percentage = calculate_percentage(total_score, total_questions)
    
    def print_result(name, percentage):
        """Prints pass/fail message based on percentage."""
        if percentage >= 50:
            print(f"Congratulations {name}, you passed with {percentage:.1f}%")
        else:
            print(f"Sorry {name}, you failed with {percentage:.1f}%.")
    
  
    print_result(candidate_name, percentage)

if __name__ == "__main__":
    candidate_name = input("Enter your name: ")
    run_cbt(candidate_name)


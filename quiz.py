# 1. SETUP: List of dictionaries
questions = [
    {
        "question": "Which fruit is yellow?",
        "options": ["A. Apple", "B. Banana", "C. Orange"],
        "correct_answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5"],
        "correct_answer": "B"
    },
    {
        "question": "Which fruit is red?",
        "options": ["A. Apple", "B. Banana", "C. Mango"],
        "correct_answer": "A"
    }
]

# Function to calculate percentage
def get_percentage(score, total):
    return (score / total) * 100


# 2. EXECUTE: Loop through questions
score = 0

for q in questions:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)
    
    # 3. INTERACT
    answer = input("Enter A, B or C: ").upper()
    
    # 4. EVALUATE
    if answer == q["correct_answer"]:
        print("Correct ")
        score += 1
    else:
        print("Wrong ")


# 5. OUTPUT
total = len(questions)
percentage = get_percentage(score, total)

print("\nFinal Score:", score, "/", total)
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("You Passed ")
else:
    print("You Failed ")
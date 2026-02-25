name=input("Please enter your your name: ")
print(f"HELLO! {name} all the best for your pop quiz")
total_score = 0
total_fail = 0

# Define the test bank with quiz questions

test_bank = [
    {
        "prompt": "What is the capital of Australia?",
        "options": ["A) Melbourne", "B) Sydney", "C) Adelaide"],
        "answer": "B"
    },
    {
        "prompt": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5"],
        "answer": "B"
    },
    {
    "prompt":"what is the color of the sky?",
    "options": ["A) pink", "B) blue", "C) black"],
    "answer": "B"
    },

    {
        "prompt":"whos is the founder of MAAUN?",
    "options": ["A) Prof Dr Israr", "B) Prof Gwarzo", "C) Prof Ibrahim"],
    "answer": "B"

    },
    {
        "prompt":"What is the color of Nigerian flag",
    "options": ["A) green white green", "B) white green white", "C) white only"],
    "answer": "A"
    }
]

# Iterating through the list of dictionaries
for q in test_bank:
    print("\n" + q["prompt"])
    for option in q["options"]:
        print(option)
        
    user_answer = input("Give your answer: ") 
    
    if user_answer == q["answer"]:
        print(f"Correct!{name}")
        total_score += 1
    else:
        print("Incorrect.")
        total_score = total_score - total_fail
        

#score =total_score
def compute_percentage(s):
    percentage = (s)*100
    if percentage >= 50:
        print("Pass")
    else: 
      print("Fail")
compute_percentage(total_score)







# Do it now: Write a simple `while` loop that acts as a 10-second timer, printing the seconds counting down from 10 to 0.

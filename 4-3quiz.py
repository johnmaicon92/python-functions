"""
Task 3: Score the quiz and give the user feedback on their performance.
"""

questions =[
    "What is 2 plus 9?",
    "What animal classification is a turtle?",
    "what is 30 minus 14?",
    "Is a woodpecker a specie of bird?"
]

correct_answers = [11, "reptile", 16, True]
answer_types = [int, str, int, bool]

score = 0

for i in range (len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if type(correct_answers[i]) == bool:
            converted_answers = user_answer.lower() in ["true", "t", "yes", "y", "1"]
        else:
            converted_answers = answer_types[i](user_answer)

        if converted_answers == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    except ValueError:
        print("Invalid input type.")

print(f"Your final score is {score}/{len(questions)}.")

          
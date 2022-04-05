from questions import question_prompts
from question_class import Question

name = input('Please enter your name ')
print(f"May The Force Be With You {name}")


questions = [
    # Assigns correct answer to questions in list
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"{name} got {score} out of {str(len(questions))} questions correct")


run_quiz(questions)
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
    """
    Fuction loops through questions and checks answer given
    against correct answer. If correct answer given
    then score increases by 1.
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        answer = answer.lower()
        if answer == question.answer:
            score += 1
    print(f"{name} got {score} out of {str(len(questions))} questions correct")


def play_again():
    """
    Function takes user input and determines
    whether to play game again.
    """
    response = input("Do you want to play again? (y/n)")
    response = response.lower()

    if response == "y":
        return True
    else:
        return False


run_quiz(questions)

while play_again():
    run_quiz(questions)
print(f"Goodbye {name}")
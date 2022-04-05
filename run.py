from questions import question_prompts
from question_class import Question

print("""
  ____ _____  _    ____   __        ___    ____  ____     ___  _   _ ___ _____
 / ___|_   _|/ \  |  _ \  \ \      / / \  |  _ \/ ___|   / _ \| | | |_ _|__  /
 \___ \ | | / _ \ | |_) |  \ \ /\ / / _ \ | |_) \___ \  | | | | | | || |  / / 
  ___) || |/ ___ \|  _ <    \ V  V / ___ \|  _ < ___) | | |_| | |_| || | / /_ 
 |____/ |_/_/   \_\_| \_\    \_/\_/_/   \_\_| \_\____/   \__\_\\___/|___/____|
                                                                              
""")

name = input("Please enter your name\n")
print(f"May The Force Be With You {name}\n")
print("*********************************")


questions = [
    # Assigns correct answer to questions
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b")
]


def run_quiz(questions):
    """
    Function loops through questions and checks answer given
    against correct answer. If correct answer given
    then score increases by 1.
    """
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        while answer not in {'a', 'b', 'c'}:
            answer = input("Invalid answer, try again").lower()
        if answer == question.answer:
            score += 1
            print(f"Well done {name}. That is correct\n")
        else:
            print(f"Sorry {name}. That answer is incorrect\n")
    print(f"{name} got {score} out of {len(questions)} questions correct")


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
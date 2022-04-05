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
print(f"\nMay The Force Be With You {name}\n")
print("*********************************")


questions = [
    # Assigns correct answer to questions
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "c"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "c"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "b"),
    Question(question_prompts[16], "c"),
    Question(question_prompts[17], "a"),
    Question(question_prompts[18], "c"),
    Question(question_prompts[19], "a")
]


def run_quiz():
    """
    Function loops through questions and checks answer given
    against correct answer. If correct answer given
    then score increases by 1.
    """
    score = 0
    for question in questions:
        # Converts user answer to lower case
        answer = input(question.prompt).lower()
        while answer not in {'a', 'b', 'c'}:
            # User input validation
            answer = input("Invalid answer, try again").lower()
        if answer == question.answer:
            # Increases score by 1
            score += 1
            print(f"Well done {name}. That is correct\n")
        else:
            print(f"Sorry {name}. That answer is incorrect\n")

        print("*********************************")

    print(f"{name} got {score} out of {len(questions)} questions correct")


def play_again():
    """
    Function takes user response and determines
    whether to play game again.
    """
    response = input("Do you want to play again? (y/n)")
    response = response.lower()

    if response == "y":
        return True
    else:
        return False


run_quiz()

while play_again():
    run_quiz()
print(f"\nGoodbye {name}")

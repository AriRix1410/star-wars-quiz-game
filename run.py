from questions import question_prompts
from question_class import Question
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Star Wars Quiz High Scores')

player_scores = SHEET.worksheet('player_scores')

data = player_scores.get_all_values()
print(data)


print("""
  ____ _____  _    ____   __        ___    ____  ____     ___  _   _ ___ _____
 / ___|_   _|/ \  |  _ \  \ \      / / \  |  _ \/ ___|   / _ \| | | |_ _|__  /
 \___ \ | | / _ \ | |_) |  \ \ /\ / / _ \ | |_) \___ \  | | | | | | || |  / / 
  ___) || |/ ___ \|  _ <    \ V  V / ___ \|  _ < ___) | | |_| | |_| || | / /_ 
 |____/ |_/_/   \_\_| \_\    \_/\_/_/   \_\_| \_\____/   \__\_\\___/|___/____|
                                                                              
""")

name = input("Please enter your name\n")
print(f"Hello, {name}.\n")


def start_game():
    """
    Function asks user if they are ready to start,
    if user input is yes then message will be displayed
    to the user and the quiz will begin. Any other input
    is deemed invalid.
    """
    if input("Are you ready to start the quiz? (y)\n").lower() == "y":
        print(f"\nMay The Force Be With You, {name}.\n")
        print("*********************************")
        run_quiz()
    else:
        print("Invalid answer, try again\n")
        start_game()


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
            answer = input("Invalid answer, try again\n").lower()
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
    whether to play game again. If yes then run_quiz runs,
    if no then goodbye message will display.
    """
    response = input("Do you want to play again? (y/n)\n").lower()

    while response not in {'y', 'n'}:
        # User input validation
        response = input("Invalid answer, try again\n").lower()
    if response == "y":
        return True
    else:
        return False


start_game()

while play_again():
    run_quiz()
print(f"\nGoodbye {name}")

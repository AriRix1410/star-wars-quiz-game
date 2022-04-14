import gspread
from google.oauth2.service_account import Credentials
from questions import question_prompts
from question_class import Question

player_scores = ["", ""]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Star Wars Quiz High Scores')

questions = [
    # Assigns correct answer to questions
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "d"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "c"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "b"),
    Question(question_prompts[16], "c"),
    Question(question_prompts[17], "b"),
    Question(question_prompts[18], "c"),
    Question(question_prompts[19], "a")
]

print("""
  ____ _____  _    ____   __        ___    ____  ____     ___  _   _ ___ _____
 / ___|_   _|/ \  |  _ \  \ \      / / \  |  _ \/ ___|   / _ \| | | |_ _|__  /
 \___ \ | | / _ \ | |_) |  \ \ /\ / / _ \ | |_) \___ \  | | | | | | || |  / /
  ___) || |/ ___ \|  _ <    \ V  V / ___ \|  _ < ___) | | |_| | |_| || | / /
 |____/ |_/_/   \_\_| \_\    \_/\_/_/   \_\_| \_\____/   \__\_\\___/|___/____|
""")

print("Would you like to test your Star Wars knowledge?")
print("You will be asked a total of 20 questions")
print("These questions are all multiple choice (a, b, c or d)")
print("To lock in your answers, type a letter and hit enter\n")


def get_name():
    """
    Get name input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, must be a string of maximum 6 characters
    and contain only letters and numbers.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        global NAME
        NAME = input("""Please enter your name
(Maximum of 6 characters. Letters and numbers only.)\n""")

        if check_name(NAME):
            print(f"\nHello, {NAME}.\n")
            break

    return NAME


def check_name(NAME):
    """
    Inside the try, validates user's input for an inputted name.
    ValueError will be raised for names longer than 6 characters,
    using characters which are deemed invalid or for lack of
    a name entry.
    """
    try:
        if not NAME:
            raise ValueError("Please enter your name")
        if len(NAME) > 6:
            raise ValueError("Name contains too many characters.")
        if not NAME.isalnum():
            raise ValueError("Invalid characters used.")
    except ValueError as e:
        print(f"Invalid data: {e} Try again.\n")
        return False

    return True


def start_game():
    """
    Function asks user if they are ready to start,
    if user input is yes then message will be displayed
    to the user and the quiz will begin. Any other input
    is deemed invalid.
    """
    if input("Are you ready to start the quiz? (y)\n").lower() == "y":
        print(f"\nMay The Force Be With You, {NAME}.\n")
        print("*********************************")
        run_quiz()
    else:
        print("Invalid answer, try again\n")
        start_game()


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
        while answer not in {'a', 'b', 'c', 'd'}:
            # User input validation
            answer = input("Invalid answer, try again\n").lower()
        if answer == question.answer:
            # Increases score by 1
            score += 1
            print(f"Well done {NAME}. That is correct\n")
        else:
            print(f"Sorry {NAME}. That answer is incorrect\n")

        print("*********************************")

    print(f"{NAME} got {score} out of {len(questions)} questions correct")
    # Adds new row to worksheet with user name and score
    SHEET.worksheet('high_scores').append_row([NAME, score])


def play_again():
    """
    Function takes user response and determines
    whether to play game again. If yes then run_quiz runs,
    if no then goodbye message will display.

    Initial code taken from [Bro Code]
    https://www.youtube.com/watch?v=yriw5Zh406s&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&index=2
    """
    response = input("Do you want to play again? (y/n)\n").lower()

    while response not in {'y', 'n'}:
        # User input validation
        response = input("Invalid answer, try again\n").lower()
    if response == "y":
        return True
    else:
        return False


def show_high_scores():
    """
    Retrieves all values from worksheet and converts scores into
    integers. Sorts scores numerically from highest to lowest and
    then displays from highest to lowest.
    """
    # gets all data, excluding headings
    all_stored_data = SHEET.worksheet('high_scores').get_all_values()[1:]

    # converts data in scores column to integers
    for num_data in all_stored_data:
        num_data[1] = int(num_data[1])

    # sorts data by scores column in descending order
    sorted_data = sorted(all_stored_data, key=lambda x: x[1], reverse=True)

    names_data = [el[0] for el in sorted_data]
    scores_data = [el[1] for el in sorted_data]

    print('\nHigh Scores\n')

    # prints top 5 high scores
    for i in range(5):
        print(str(names_data[i]) + "\t" + str(scores_data[i]))


def main():
    """
    Run all program functions
    """
    get_name()
    check_name(NAME)
    # Initial code from [Bro Code], link in README.md
    start_game()
    while play_again():
        run_quiz()
    print(f"\nGoodbye {NAME}")
    show_high_scores()


main()

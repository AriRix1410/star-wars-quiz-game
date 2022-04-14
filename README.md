# Star Wars Quiz Game

Star Wars Quiz Game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The aim of this game is to test Star Wars fans on their Star Wars knowledge and provide a source of entertainment. This quiz is aimed at both adults and children alike who have an interest in the Star Wars universe.

The live link to this project can be found here - http://star-wars-quiz-game.herokuapp.com/

![Responsive Mockup](/assets/images/mock-up.png)

## How To Play

The user is required to enter a name and will then be asked if they are ready to begin in order for the quiz to start.

Users will be asked 20 multiple choice questions and must provide an answer from the options given (a, b, c or d).

To submit their answer, users must type a corresponding letter option for their chosen answer and hit enter.

Users will then see if they were correct or incorrect with that answer.

At the end of the quiz users will be provided with how many answers they got correct.

## Features 

### Existing Features

- __Title Screen__
  - Upon first accessing the page, users will be presented with a title, "Star Wars Quiz" in ASCII.
  - ASCII has been used because it improves the look of the quiz and clearly tells users what the game is.
  - Also found here are a brief description about what the quiz entails, how to play the game and an input request for the users name.

![Title Screen](/assets/images/home-screen.png)

- __Name Input__
  - Users are required to input a name.
  - This is asked at this stage in the game in order to provide a more personalised experience from the start.
  - Names are required to be a maximum of 6 characters in length (this improved the appearance of the high scores at the end), and contain only letters and numbers.
  - If names meet the validation requirements then a greeting will be displayed and the user will be asked if they are ready to start the quiz.

  ![Valid Name](/assets/images/greeting.png)
  ![Start Quiz](/assets/images/start-quiz.png)
  

  - If names do not meet the validation requirements then a message will be displayed as to which validation requirement the name fails and to enter another name.

  ![Name Too Long](/assets/images/invalid-data-long.png) 
  ![Invalid Characters](/assets/images/invalid-data-char.png)

- __Questions__
  - Users will be asked a total of 20 questions.
  - These questions are all multiple choice with answers either a, b, c or d. These options are not case sensitive so if the user is playing the game in CAPS then the answers will still display as correct or incorrect.
  - If answers do not meet the validation requirements then a message will be displayed stating invalid answer and to try again.

  ![Invalid Answer](/assets/images/invalid-ans.png)

  - Upon succesfully submitting an answer, users will be told whether they are correct or incorrect and the next question will be asked.

  ![Correct Answer](/assets/images/correct-ans.png)
  ![Incorrect Answer](/assets/images/incorrect-ans.png)

- __End of Quiz__
  - At the end of the quiz, users will be told how many correct answers they got out of 20 and asked if they would like to play again.
  - If users choose to play the game again then they will be taken back to the start of the questions.
  - If users choose not to play again then they will recieve a good bye message and be shown the High Scores.
  - Names and scores are stored in a Google Sheets worksheet via API.

  ![End of Quiz](/assets/images/quiz-end.png)

### Features Left to Implement

- A feature I would like to add in the future is to have more questions and to randomise them so users would have to answer any 20 guestions that are randomly selected by the computer, in order to provide a better user experience.
- I would also like for users to be able to see their previous scores.

## Data Models

Google Sheets was used to store the data for the user's name and score. When the quiz ends this data is sorted numerically in order of highest scores to lowest and when the user no longer wants to play, the top 5 highest scores are displayed.

![High Scores Sheet](/assets/images/scores-sheet.png)

This project also contains a questions Class in order to store both the prompts to the questions and also the question answers.

## Logic

### Flowchart

![Flowchart](/assets/images/flowchart.png)

## Testing

I have manually tested this project in the following ways:

- All code has been passed through the [PEP8 Python Validator](http://pep8online.com/checkresult) with no issues.

![PEP8 Run](/assets/images/pep8.png)
![PEP8 Class](/assets/images/pep8-class.png)
![PEP8 Questions](/assets/images/pep8-questions.png)

- Given invalid inputs such as names that are over 6 characters in length, names that contain symbols, answers other than a, b, c or d and inputs different to y or n when only y or n are required.
- Tested in my local terminal on Gitpod and in the Code Institute Heroku terminal.

### Bugs

- When trying to set up user input validation for my questions, I encountered an issue where the error message would print but would still accept the input and proceed further in the game. This was due to me putting the if and while statements in my loop in the wrong order. When switched, the code performed as expected.
- When writing the code for the high scores, the scores after sorting where sorted alphanumerically, this caused the high scores to be incorrect as numbers such as 11 and 14 where lower than other scores with a lower value as the first digit was lower. After recieving help in Stack Overflow, I was able to convert the scores into integers and then the scores were in the correct order.
- Initially, instead of get_all_values, I used col_values. Although this did sort the scores, I realised that by doing this, the corresponding names to the scores were not being printed and instead was just the 5 first name entries on Google sheets. By using get_all_values instead, I was able to sort by the scores column but also print the correct names for those scores.
- By using the method above, I encountered another problem where it was sorting the first column which contains the name data as opposed to the second column which contained the score data. This was due to a problem with my indexing being incorrect. After researching again, I was able to re-write this so that the data being sorted was from the scores column and the issue was fixed.

### Unfixed Bugs

- No unfixed bugs

### Validator Testing

- [PEP8 Python Validator](http://pep8online.com/checkresult) - no issues

## Deployment

- This project has been deployed to Heroku. The steps to deploy are as follows: 
  - Create a new Heroku app
  - In the settings tab, set two Config Vars, one for CREDS.json file, and one setting PORT to 8000 
  - Scroll down and set the build packs to Python and NodeJS, in that order
  - Click on depoly and link the Heroku app to the Github repositary
  - Scroll down to manual deploy and click deploy branch
  - After some time, a message will be displayed stating the app was successfully deployed
  - You can then click on view to see the deployed project.

## Credits  

### Content 

- The initial inspiration and code for this project was taken from [Mike Dane](https://www.youtube.com/watch?v=SgQhwtIoQ7o) and [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&index=2), then edited and expanded for my own requirements.
- [Stack Overflow](https://stackoverflow.com) was a great source of information throughout the project but was particularly used for help with user input validation [here](https://stackoverflow.com/questions/71757895/user-input-validation-in-python), when trying to sort the high scores [here](https://stackoverflow.com/questions/71785967/sorting-column-b-google-sheets-api-python) where I ended up physically asking for help after struggling for a considerable amount of time, with the same issues.
- [Code Institute](https://learn.codeinstitute.net/) Python Essentials tutorials were consulted throughout for clarification and understanding, especially the Love Sandwiches project which was inspiration for the get_name and check_name functions.
- [Real Python](https://realpython.com/python-sort/) and [DelftStack](https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/) with help on sorting.
- [Geeks For Geeks](https://www.geeksforgeeks.org/python-get-first-and-last-elements-of-a-list/) and [Career Karma](https://careerkarma.com/blog/python-indexerror-list-index-out-of-range/) with help on list comprehension.
- The ASCII title in this project came from [Patorjk](https://patorjk.com/software/taag/#p=display&f=Standard&t=STAR%20WARS%20QUIZ)
- Questions for the quiz have came from [Ultimate Quiz Questions](https://www.ultimatequizquestions.com/star-wars-quiz-questions/), [Radio Times](https://www.radiotimes.com/tv/sci-fi/pub-quiz-star-wars/) and [Thought Catalog](https://thoughtcatalog.com/katee-fletcher/2020/04/star-wars-trivia-questions/)

### Special Thanks

- Thanks to my mentor Caleb Mbakwe for his insight and guidance throughout.
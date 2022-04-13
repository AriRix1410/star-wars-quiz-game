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
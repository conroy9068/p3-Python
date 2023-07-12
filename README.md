# Tic Tac Toe

Welcome to Tic Tac Toe!

This is a simple game of Tic Tac Toe that you can play in your browser. It is built using Python.

Users are asked to enter their name and then choose whether they want to be X or O. The game will then begin.

[Live Site](https://p3-python-tic-tac-toe-588f3ed03006.herokuapp.com/).

## Table of Contents
1. [Control Flow Diagram](#control-flow-diagram)
2. [Game Flow](#game-flow)
3. [Game Rules](#game-rules)
4. [Features](#features)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Technology Used](#technology-used)
8. [Creating the Heroku app](#creating-the-heroku-app)
9. [Resources](#resources)


## Control Flow Diagram
I used diagram.net to design the control flow for the game. It can be viewed in full via the link below.

[Link to Control Flow Diagram](https://drive.google.com/file/d/1XJ4Ax3YYQIWj0WAvEqjQwolLRIkTeff6/view?usp=sharing)

![Control Flow](https://github.com/conroy9068/p3-Python/blob/main/assets/images/control-flow.png)

## Game Flow

1. The game begins by asking each user to enter their name. This is stored in a variable called `player_name`.

![Start Screen](https://github.com/conroy9068/p3-Python/blob/main/assets/images/start.png)

![Enter player names](https://github.com/conroy9068/p3-Python/blob/main/assets/images/enter-player-names.png)

2. The user is then asked to choose whether they want to be X or O. This is stored in a variable called `player_symbol`.

![Choose symbol](https://github.com/conroy9068/p3-Python/blob/main/assets/images/chose-x-or-o.png)

3. The game then begins. The user is asked to choose a number from 1-9. This is stored in a variable called `player_choice`. This step is repeated until a winner is found or the board is full.

![Choose move](https://github.com/conroy9068/p3-Python/blob/main/assets/images/single-game-start.png)

4. The game will then check if the user has won after each move. If they have, the game will end and display the winner the user will then be asked if they want to play again.

![Winner](https://github.com/conroy9068/p3-Python/blob/main/assets/images/winner.png)

5. If the user has not won, the game will check if the board is full. If it is, the game will end and display a message saying it is a draw. The user will then be asked if they want to play again.

![Draw](https://github.com/conroy9068/p3-Python/blob/main/assets/images/draw-game.png)

6. If the user chooses to quit the game, the scoreboard with the final scores will be displayed. And a record of the game will be added to the Google Sheet.

![Scoreboard](https://github.com/conroy9068/p3-Python/blob/main/assets/images/quit-game-result.png)

![Google Sheet](https://github.com/conroy9068/p3-Python/blob/main/assets/images/gsheet-db.png)

## Game Rules

1. The game is played on a grid that's 3 squares by 3 squares.
2. Players choose their symbol ('X' or 'O') before starting each game. 
3. Players take turns putting their marks in empty squares.
4. The first player to get 3 of her marks in a row (up, down, across, or diagonally).
5. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Here's what the board looks like:

            1   |   2   |   3   
        ------------------------
            4   |   5   |   6   
        ------------------------
            7   |   8   |   9   

Players will choose a number from 1-9 to place their mark in the corresponding square.

## Features

### Existing Features

- **Google Sheet** - The game will add a record of the game to a Google Sheet. This will include the date and time, the player names, the winner and the final score.

    [Link to Google Sheet](https://docs.google.com/spreadsheets/d/1CFEjZdeQxCWNoqitT0pSJT--rjcz3kQOPFTuXDeY4S4/edit?usp=sharing)

- **Timer** - There is a timer delaying the introduction test so that just the ascii art is displayed for a few seconds before the game begins. 

    [Screenshot](https://github.com/conroy9068/p3-Python/blob/main/assets/images/sleep-timer.png)

- **Move Validation** - The game will check if the user has entered a valid move. If they have not, they will be asked to enter a valid move. 
    
    [Screenshot](https://github.com/conroy9068/p3-Python/blob/main/assets/images/gameboard-move-validation.png)

### Features Left to Implement

- **AI** - I would like to add an AI so that the user can play against the computer.

- **Color/UI** - I would like to add color and a nicer UI to the game to make it more visually appealing.

## Testing

I used the following tools to test the application:

- [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8) - Used to format the code to PEP8 standards

- [pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) - Used to check the code for errors

- Testing locally - Testing was carried out during the development of the project. I used the terminal to run the application locally and test the functionality.

- [Heroku](https://p3-python-tic-tac-toe-588f3ed03006.herokuapp.com/) - The application was deployed to Heroku and tested there.

- CI Python Linter Test.
![CI Python Linter Test](https://github.com/conroy9068/p3-Python/blob/main/assets/images/ci-python-linter.png)

#### Manual Testing

##### Testing Name Inputs
| Action  | Expected Result | Pass/Fail |
| ------------- | ------------- | ------------- |
| Game is started using python run.py  | The program outputs introduction and rules and then "Player 1 Enter the name :", and waits for the user to enter a name  | Pass |
| Input "David" for player 1's name | The program accepts the input and moves on to player 2  | Pass |
| Hit enter for player 1's name  | The program outputs "Invalid input. Only alphabets are allowed. Try again.", and prompts for player 1's name again | Pass |
| Input "!123" for player 1's name  | The program outputs "Invalid input. Only alphabets are allowed. Try again.", and prompts for player 1's name again | Pass |
| After player 1's name has been entered, player 2 is prompted for a name  | The program outputs "Player 2", and waits for the user to enter a name  | Pass |
| Input "John" for player 2's name | The program accepts the input and continues with the rest of the program  | Pass |
| Hit enter for player 2's name  | The program outputs "Invalid input. Only alphabets are allowed. Try again.", and prompts for player 2's name again | Pass |
| Input "!1234" for player 2's name | The program outputs "Invalid input. Only alphabets are allowed. Try again.", and prompts for player 2's name again  | Pass |
| After both names have been entered, the program starts. | The program starts and displays the player names in the score board and then asks player 1 to chose a symbol. | Pass |

#### Testing Main Menu Inputs

| Action  | Expected Result | Pass/Fail |
| ------------- | ------------- | ------------- |
| At the start of the main menu loop, the current player is prompted to make a choice  | The program outputs "Turn to choose for", followed by the current player's name. It then lists the possible options: 1 for X, 2 for O, 3 to Quit | Pass |
| Input a non-numeric value or string | The program catches the error and outputs "Wrong Input!!! Try Again\n", prompting the player for their choice again | Pass |
| Input a number other than 1, 2, or 3 | The program outputs "Wrong Choice!!!! Try Again\n", and prompts the player for their choice again | Pass |
| Selecting 1 for the current player's choice | The program assigns the symbol 'X' to the current player and 'O' to the other player, and moves on to the next part of the game | Pass |
| Selecting 2 for the current player's choice | The program assigns the symbol 'O' to the current player and 'X' to the other player, and moves on to the next part of the game | Pass |
| Selecting 3 for the current player's choice | The program outputs "Final Scores", shows the score board, and exits the game | Pass |

#### Testing Game Board Inputs
| Action  | Expected Result | Pass/Fail |
| ------------- | ------------- | ------------- |
| When the game loop starts, the game board is printed and the current player is prompted to choose a box | The game board is displayed with all positions empty and the program outputs "Player [name] turn. Which box? :" | Pass |
| Input a non-numeric value or string for the box choice | The program catches the ValueError and outputs "Wrong Input!!! Try Again", prompting the player for their choice again | Pass |
| Input a number less than 1 or greater than 9 for the box choice | The program outputs "Wrong Input!!! Try Again", and prompts the player for their choice again | Pass |
| Choose a box that's already been filled | The program outputs "Place already filled. Try again!!", and prompts the player for their choice again | Pass |
| Choose an empty box for the current player's move | The program fills the chosen box with the current player's symbol, checks for win or draw, and switches to the other player | Pass |
| Current player gets three of their symbols in a row, column, or diagonal | The game board is printed showing the winning line, the program outputs "Player [name] has won the game!!", and the game ends | Pass |
| All boxes get filled without a win (draw condition) | The game board is printed showing the full board, the program outputs "Game Drawn", and the game ends | Pass |


## Bugs
### Fixed Bugs
- **Invalid Number in Menu causing app to crash** - If the user enters a number that is not 1, 2 or 3 in the menu, the app will crash. This was fixed by adding a continue statament.

- **Blank name entry would cause the game to crash** - If the user entered a blank name, the game would crash. This was fixed by using the `isalpha()` function to check if the name entered was a string. It also stopped users from user numbers as a name.

    [Screenshot](https://github.com/conroy9068/p3-Python/blob/main/assets/images/bug-wrong-number-at-menu-causes-crash.png)
## Technology Used
- **Python** - The application was built using Python
- **Heroku** - Used to deploy and host the application
- **Github** - Used to store the code
- **Visual Studio Code** - IDE used to write the code
- **Git** - Used to push the code to Github and create version control
## Creating the Heroku app

The project was deployed to Heroku using the Code Institute template.

Here are the steps to follow to deploy your project to Heroku:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
2. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
3. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
4. For the key put "CRED" and for the value put the contents of your `creds.json` file (you can copy and paste it).
5. In the buildpacks section, add the following packs in the order below:

    1. `heroku/python`
    2. `heroku/nodejs`
6. Now click on the tab "Deploy" > "Deployment method" and select GitHub.
7. Confirm the linking of the Heroku app to the correct GitHub repository.
8. In the "Manual Deploy" section below, select the main branch then click "Deploy Branch".
9. The site will now be deployed. You can click the "Open App" button at the top of the page to launch it.

## Resources

- [Tic Tac Toe Tutorial](https://www.askpython.com/python/examples/tic-tac-toe-using-python)
- [Google sheet API setup](http://ai2.appinventor.mit.edu/reference/other/googlesheets-api-setup.html)
- [Python sleep function](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/)
- [ASCII Art](https://ascii.co.uk/art/tictactoe)
- [Is Alpha Function](https://www.w3schools.com/python/ref_string_isalpha.asp)


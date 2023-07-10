# Tic Tac Toe

Welcome to Tic Tac Toe!

This is a simple game of Tic Tac Toe that you can play in your browser. It is built using Python.

Users are asked to enter their name and then choose whether they want to be X or O. The game will then begin.

[Live Site](https://p3-python-tic-tac-toe-588f3ed03006.herokuapp.com/).

## Table of Contents


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

- **Google Sheet** - The game will add a record of the game to a Google Sheet. This will include the date and time, the player names, the winner and the final score.[Link to Google Sheet](https://docs.google.com/spreadsheets/d/1CFEjZdeQxCWNoqitT0pSJT--rjcz3kQOPFTuXDeY4S4/edit?usp=sharing)

- **Timer** - There is a timer delaying the introduction test so that just the ascii art is displayed for a few seconds before the game begins. [Screenshot](https://github.com/conroy9068/p3-Python/blob/main/assets/images/sleep-timer.png)

- **Move Validation** - The game will check if the user has entered a valid move. If they have not, they will be asked to enter a valid move. [Screenshot](https://github.com/conroy9068/p3-Python/blob/main/assets/images/gameboard-move-validation.png)

### Features Left to Implement

## Technology Used
- Python
    - Used to create the application

- Heroku
    - Used to deploy and host the application

- Github
    - Used to store the code

- Visual Studio Code
    - IDE used to write the code

- Git
    - Used to push the code to Github and create version control



## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

## Resources

- [Tic Tac Toe Tutorial](https://www.askpython.com/python/examples/tic-tac-toe-using-python)
- [Google sheet API setup](http://ai2.appinventor.mit.edu/reference/other/googlesheets-api-setup.html)
- [Python sleep function](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/)
- [ASCII Art](https://ascii.co.uk/art/tictactoe)

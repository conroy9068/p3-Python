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

1. The game begins by asking the user to enter their name. This is stored in a variable called `player_name`.

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

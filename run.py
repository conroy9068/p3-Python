"""
Tic Tac Toe Game
This python code defines a text-based Tic Tac Toe game
that can be played in the terminal.It supports two players,
each player enters their names at the beginning of the game.
The players then take turns selecting their symbol and
choosing where to place it. The players place their symbol
in spaces until one player wins by having three in a row,
or until the game is a draw because all spaces on the board
are filled then there is no winner.
"""

from time import sleep
import os
import json
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds_json = os.getenv('CREDS')
creds_dict = json.loads(creds_json)

CREDS = Credentials.from_service_account_info(creds_dict)
SCOPED_CREDS = CREDS.with_scopes(scope)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Tic Tac Toe Score Database')
WORKSHEET = SHEET.get_worksheet(0)

# Function to print Tic Tac Toe Table


def print_table(values):
    """
    Prints a table using the provided list of values.

    Args:
        values (list): A list of 9 values representing the table cells.
        The values should be provided in the following order:
                [0] [1] [2]
                [3] [4] [5]
                [6] [7] [8]

    Returns:
        None

    Example:
        >>> values = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        >>> print_table(values)

                     |     |
                  X  |  O  |  X
                _____|_____|_____
                     |     |
                  O  |  X  |  O
                _____|_____|_____
                     |     |
                  X  |  O  |  X
                     |     |
    """
    print("\n")
    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}")
    print("\t     |     |")
    print("\n")

# Function to print the score-board


def print_score_board(score_board):
    """
    Prints the score board with player names and their scores.

    Args:
        score_board (dict): A dictionary containing player
        names as keys and their scores as values.

    Returns:
        None

    Example:
        >>> score_board = {'Player 1': 10, 'Player 2': 5}
        >>> print_score_board(score_board)

        --------------------------------
                      SCOREBOARD
        --------------------------------
           Player 1        10
           Player 2        5
        --------------------------------
    """
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Function to check for winner


def check_win(player_pos, cur_player):
    """
    Checks if the current player has won the game based on their positions.

    Args:
        player_pos (dict): A dictionary containing player positions as keys and
            a list of positions occupied by each player as values.
        cur_player (str): The current player's identifier.

    Returns:
        bool: True if the current player has won, False otherwise.

    Example:
        >>> player_pos = {'Player 1': [1, 2, 3], 'Player 2': [4, 5, 6]}
        >>> cur_player = 'Player 1'
        >>> check_win(player_pos, cur_player)
        True
    """
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]
    # Loop to check if any winning combination is satisfied
    for x_position in soln:
        if all(y in player_pos[cur_player] for y in x_position):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False

# Function to check if the game is drawn


def check_draw(player_pos):
    """
    Checks if the game is drawn.

    Args:
        player_pos (dict): A dictionary containing player positions as keys and
            a list of positions occupied by each player as values.

    Returns:
        bool: True if the game is drawn, False otherwise.

    Example:
        >>> player_pos = {'Player 1': [1, 2, 3], 'Player 2': [4, 5, 6]}
        >>> check_draw(player_pos)
            False
    """
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False

# Function for a single game of Tic Tac Toe


def single_game(player):
    """
    Runs a single game of Tic Tac Toe.

    Args:
        current_player (str): The current player's identifier.

    Returns:
        str: The winning player's identifier, or 'D' if the game is drawn.

    Example:
        >>> single_game('Player 1')
        Player 1
    """
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_table(values)
        try:
            print("Player ", player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue

        # Updating grid status
        values[move-1] = player

        # Updating player positions
        player_pos[player].append(move)

        # Function call for checking win
        if check_win(player_pos, player):
            print_table(values)
            print("Player ", player, " has won the game!!")
            print("\n")
            return player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_table(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switching player moves
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


if __name__ == "__main__":

    print("""
    888   d8b        888                   888
    888   Y8P        888                   888
    888              888                   888
    888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
    888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
    888   888888     888   .d888888888     888   888  88888888888
    Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
    "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888
    """)

    sleep(2)

    print("""
    Welcome to Tic Tac Toe!
    In this game, two players will take turns marking the spaces in a 3x3 grid.
    The players have the freedom to choose whether to play as 'X' or 'O'
    after each game.The player who succeeds in placing three of their
    marks in a horizontal, vertical, or diagonal row is the winner.
    It's a fun game that you can play anytime to challenge your
    strategic abilities.

    Rules of the game:
    1. The game is played on a grid that's 3 squares by 3 squares.
    2. Players choose their symbol ('X' or 'O') before starting each game.
    3. Players take turns putting their marks in empty squares.
    4. The first player to get 3 of her marks in a row
        (up, down, across, or diagonally).
    5. When all 9 squares are full, the game is over.
        If no player has 3 marks in a row, the game ends in a tie.

    Here's what the board looks like:

       1   |   2   |   3
    ------------------------
       4   |   5   |   6
    ------------------------
       7   |   8   |   9

    Players will choose a number from 1-9 to place their mark
    in the corresponding square.
    Enjoy playing Tic Tac Toe!
    """)

    print("Player 1")
    while True:
        player1 = input("Enter the name : ")
        if player1.isalpha():
            break
        else:
            print("Invalid input. Only alphabets are allowed. Try again.")
    print("\n")
    print("\n")
    print("Player 2")
    while True:
        player2 = input("Enter the name : ")
        if player2.isalpha():
            break
        else:
            print("Invalid input. Only alphabets are allowed. Try again.")
    print("\n")
    current_player = player1
    player_choice = {'X': "", 'O': ""}
    options = ['X', 'O']

    score_result = {player1: 0, player2: 0}
    print_score_board(score_result)

# Main game loop
    while True:

        print("Turn to choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Logic for players choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            print_score_board(score_result)
            # update player1's score
            WORKSHEET.update_acell('A1', f"{player1}'s Score")
            WORKSHEET.update_acell('B1', str(score_result[player1]))
            # update player2's score
            WORKSHEET.update_acell('A2', f"{player2}'s Score")
            WORKSHEET.update_acell('B2', str(score_result[player2]))
            break


        else:
            print("Wrong Choice!!!! Try Again\n")
            continue

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_result[player_won] = score_result[player_won] + 1

        print("Scores")
        print_score_board(score_result)

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

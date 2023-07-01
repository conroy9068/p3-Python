# Function to print Tic Tac Toe Table
def print_table(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
## Function for a single game of Tic Tac Toe
def single_game(current_player):
 
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_table(values)
         
        try:
            print("Player ", current_player, " turn. Which box? : ", end="")
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
        values[move-1] = current_player
 
        # Updating player positions
        player_pos[current_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, current_player):
            print_table(values)
            print("Player ", current_player, " has won the game!!")     
            print("\n")
            return current_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_table(values)
            print("Game Drawn")
            print("\n")
            return 'D'

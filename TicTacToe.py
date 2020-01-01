# --------- Global Variables -----------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"


# ------------- Functions ---------------

# plays a game of tic tac toe
def play_game():

  # shows the original game board
  display_board()

 #loops keeps on going until the game is over
  while game_still_going:

    # handles a turn
    handle_turn(current_player)

    # checks if the game is over
    check_if_game_over()

    # flips to the other player
    flip_player()
  
  #prints the result
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# displays the board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9")
  print("\n")


# handles the turn for X or O
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  #too check if the valid is suitable
  valid = False
  while not valid:

    # make sure if it is a valid input
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid Input! Choose a position from 1-9: ")
 
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # put X or O on the board
  board[position] = player

  # show the game board
  display_board()


# check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# check winner
def check_for_winner():
 
  #declare global variable
  global winner

  # check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  
  # return the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# check the row if it is in a 3 in a row
def check_rows():
  
  # declare a global variable
  global game_still_going

  # check if the row has all of the values and if it is not -
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  

  if row_1 or row_2 or row_3:
    game_still_going = False
  
  # return the result
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return None

# Check the columns for a win
def check_columns():
  
  # declare a global variable
  global game_still_going
  
  # check if all of the columbs has the same value and it is not -
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False
  
  # return the result
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return None


# check if a diagonal is 3
def check_diagonals():
  
  # declare a global variable
  global game_still_going
  
  #check if diagonal has all X or O or if they all have -
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  
  if diagonal_1 or diagonal_2:
    game_still_going = False
 
 #return the result
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None


# check if it is a tie
def check_for_tie():
 
  #declare a global variable
  global game_still_going
 
 #check if it is a tie
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False


# flip the current player
def flip_player():

  # declare a global variable
  global current_player

  #  X to O or vice versa
  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"

# Play a game of tic tac toe
play_game()
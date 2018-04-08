from IPython.display import clear_output
import random

def display_board(board):
    print_space_line()
    print_entry_line(board[0], board[1], board[2])
    print_sep_line()
    print_entry_line(board[3], board[4], board[5])
    print_sep_line()
    print_entry_line(board[6], board[7], board[8])
    print_space_line()

def print_sep_line():
    print( "###########")
    
def print_space_line():
    print( "   #   #   ")
    
def print_entry_line(entry1, entry2, entry3):
    print(f" {entry1} # {entry2} # {entry3} ")
	
def replay():
    while choice not in ['Y', 'N']:
        choice = input("Would you like to play again? Y/N: ")
        if choice.capitalize() == 'Y':
            return True
        elif choice.capitalize() == 'N':
            return False

def full_board_check(board):
    if '' not in board:
        return True
    else:
        return False
		

def choose_first():
    return random.randint(1,2)
	
def win_check(board, mark):
    if(   (board[0] == board[1] == board[2] == mark) or 
          (board[3] == board[4] == board[5] == mark) or
          (board[6] == board[7] == board[8] == mark) or
          (board[0] == board[3] == board[6] == mark) or
          (board[1] == board[4] == board[7] == mark) or 
          (board[2] == board[5] == board[8] == mark) or 
          (board[0] == board[4] == board[8] == mark) or 
          (board[6] == board[4] == board[2] == mark)):
        return True
    else:
        return False
		
def place_marker(board, marker, position):
    if board[position - 1] == '':
        board[position - 1] = marker
        return True
    else:
        print("Position already taken, please try again")
        return False
		
def player_input():
    choice = ''
    while choice == '':
        choice = input("Please select 'X' or 'O' to play: ")
        
        if choice.capitalize() == 'X':
            player1 = 'X'
            player2 = 'O'
        elif choice.capitalize() == 'O':
            player1 = 'O'
            player2 = 'X'
        else:
            choice = ''
    return (player1, player2)
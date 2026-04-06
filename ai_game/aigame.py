import random
from colorama import Fore, style
init(autoreset=True)

def display_board (board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + style.RESET_ALL
        else:
            return Fore.YELLOW + cell + style.RESET_ALL
    print(''+ colored(board[0]) +' |'+ colored(board[1]) +' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------')
    print(''+ colored(board[3]) +' |'+ colored(board[4]) +' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------')
    print(''+ colored(board[6]) +' |'+ colored(board[7]) +' | ' + colored(board[8]))
    print()

def player_choice()
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Choose your symbol (X/O): ").upper()
    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'
    
def player_move(board, symbol):
    while True:
        try:
            move = int(input(Fore.GREEN + "Enter your move (1-9): ")) - 1
            if move not in range(1, 10): or not board[move-1].isdigit():
                print(Fore.RED + "Invalid move. Please enter a number between 1 and 9 corresponding to an empty cell.")
        board[move-1] = symbol

def ai_move(board,ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy=board.copy()
            board_copy[i]=ai_symbol
            
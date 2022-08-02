"""
@author: NIDHI

"""

import utils
import heuristics_ais as ai
import minimax_ai as mm

BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def new_board():
    board = []
    for _ in range(BOARD_HEIGHT):
        c = []
        for _ in range(BOARD_WIDTH):
            c.append(None)
        board.append(c)
        
    return board

def render(board):
    print("\n    ", end="")
    for i in range(BOARD_WIDTH):
        print("",i,"  ", end="")
    print()
    
    print("  ", end="")
    for _ in range(6*BOARD_WIDTH - 1):
        print("-", end="")       
    print()
        
    for i in range(BOARD_HEIGHT):
        print(i,"|", end="")
        for j in range(BOARD_WIDTH):
            if board[i][j] is not None:
                print(" ",board[i][j]," ", end="")
            else:
                print("     ", end="")
        print("|")
        
    print("  ", end="")
    for _ in range(6*BOARD_WIDTH - 1):
        print("-", end="")
    
    print()
        
    return

def make_move(board, move, player):
    if board[move[0]][move[1]] is not None:
        raise Exception("Illegal move!")
        
    board[move[0]][move[1]] = player


def get_winner(board):
    lines = utils.get_all_line_coords(board)
    
    for line in lines:
        values = list(board[x][y] for (x,y) in line)
        
        if None not in values:
            if len(set(values)) == 1:
                return values[0]
                
    return None


def get_move(board, player, algorithm):
    if algorithm == 'minimax_ai':
        return mm.minimax_ai(board, player)
    
    else:
        func = getattr(ai, algorithm, None)
        
        if func is None:
            raise Exception("Unknown algorithm_name : " + algorithm)
            
        else:
            return func(board, player)
            
  
def play(player1_name, player2_name):
    
    players = [
        ("X", player1_name),
        ("O", player2_name)
    ]
    
    count = 0
    board = new_board()
    render(board)
    
    while count < (BOARD_HEIGHT * BOARD_WIDTH):
        player_id, player_name = players[count % 2]
            
        print(f"\nPlayer {player_id} ---> ")
        print(f"Algorithm : {player_name} ")
        
        move_coords = get_move(board, player_id, player_name)
            
        make_move(board, move_coords, player_id)
        render(board)
        
        winner = get_winner(board)
        if winner is not None:
            break
        
        count += 1
        
    
    if winner is None:
        print("\nWell that's a draw :)")
    else:
        print(f"\nThe winner is player {winner}!! Congrats on your hard-earned victory :D")
    

    
    
        
        


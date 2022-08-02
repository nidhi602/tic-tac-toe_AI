"""
@author: NIDHI

"""

import random
import utils

BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def random_ai(board, player):
    x = random.randint(0,BOARD_WIDTH - 1)
    y = random.randint(0,BOARD_HEIGHT - 1)
    
    while(board[x][y] is not None):
        x = random.randint(0,BOARD_WIDTH - 1)
        y = random.randint(0,BOARD_HEIGHT - 1)
        
    return (x,y)


def finds_winning_moves_ai(board, player):
    lines = utils.get_all_line_coords(board)
    
    for line in lines:
        player_count = 0
        none_count = 0
        
        for (x,y) in line:
            value = board[x][y]
            if value == player:
                player_count += 1
            elif value is None:
                none_count += 1
                location = (x,y)
            else:
                break
        
        if player_count == 2 and none_count == 1:
            return location
        
    return random_ai(board, player)


def finds_winning_and_losing_moves_ai(board, player):
    lines = utils.get_all_line_coords(board)
    
    block_move = None
    for line in lines:
        this_player_count = 0
        other_player_count = 0
        none_count = 0
        
        for (x,y) in line:
            value = board[x][y]
            if value == player:
                this_player_count += 1
                other_player_count = 0
            elif value is None:
                none_count += 1
                possible_move = (x,y)
            else:
                other_player_count += 1
                this_player_count = 0
                
        
        if this_player_count == 2 and none_count == 1:
            return possible_move
        
        if other_player_count == 2 and none_count == 1:
            block_move = possible_move
    
    if block_move is not None:
        return block_move
        
    return random_ai(board, player)


def is_valid_move(board, move):
    if move[0] < 0 or move[0] >= BOARD_HEIGHT:
        return False
    if move[1] < 0 or move[1] >= BOARD_WIDTH:
        return False
    if board[move[0]][move[1]] is not None:
        return False
    
    return True

def human_player(board, player):        
    while True:
        x = int(input("Enter X-coordinate: "))
        y = int(input("Enter Y-coordinate: "))
    
        move = (x,y)
        
        if is_valid_move(board, move):
            break
        else:
            print("\nIllegal move, try again!")
    
    return (x,y)
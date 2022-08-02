"""
@author: NIDHI

"""

import engine
import utils

def minimax_score(board, current_player, player_to_optimize):
    winner = engine.get_winner(board)
    
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    
    elif utils.is_board_full(board):
        return 0
    
    legal_moves = utils.get_all_legal_moves(board)
    
    scores = []
    for move in legal_moves:
        new_board = [row[:] for row in board]
        
        engine.make_move(new_board, move, current_player)
        
        opponent = utils.get_opponent(current_player)
        score = minimax_score(new_board, opponent, player_to_optimize)
        
        scores.append(score)
    
    
    if current_player == player_to_optimize:
        return max(scores)
    else:
        return min(scores)
    

    
def minimax_ai(board, player):
    best_move = None
    best_score = None
    
    legal_moves = utils.get_all_legal_moves(board)
    for move in legal_moves:
        new_board = [row[:] for row in board]
        
        engine.make_move(new_board, move, player)
        
        opponent = utils.get_opponent(player)
        score = minimax_score(new_board, opponent, player)
        
        if best_score is None or score > best_score:
            best_score = score
            best_move = move
            
    return best_move
        
        
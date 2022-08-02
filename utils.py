"""
@author: NIDHI

"""

def get_all_line_coords(board):
    num_rows = len(board)
    num_columns = len(board[0])
    lines = []
    
    for x in range(num_rows):
        row = []
        for y in range (num_columns):
            row.append((x,y))
        lines.append(row)
    
    for y in range(num_columns):
        col = []
        for x in range(num_rows):
            col.append((x,y))
        lines.append(col)
    
    dia1 = list((i,i) for i in range(num_rows))
    dia2 = list((i, num_rows - 1 - i) for i in range(num_rows))
    lines.append(dia1)
    lines.append(dia2)
    
    return lines


def is_board_full(board):
    for row in board:
        for value in row:
            if value is None:
                return False
            
    return True


def get_all_legal_moves(board):
    moves = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] is None:
                moves.append((x,y))
                
    return moves


def get_opponent(player):
    
    if player == 'X':
        return 'O'
    
    elif player == 'O':
        return 'X'
    
    else:
        raise Exception("Unknown player : " + player)
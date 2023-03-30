# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from .utils import render_board

def search(input: dict[tuple, tuple]) -> list[tuple]:
    """
    This is the entry point for your submission. The input is a dictionary
    of board cell states, where the keys are tuples of (r, q) coordinates, and
    the values are tuples of (p, k) cell states. The output should be a list of 
    actions, where each action is a tuple of (r, q, dr, dq) coordinates.

    See the specification document for more details.
    """
    # The render_board function is useful for debugging -- it will print out a 
    # board state in a human-readable format. Try changing the ansi argument 
    # to True to see a colour-coded version (if your terminal supports it).
    # print(render_board(input, ansi=True))
    board = input
    print(board)
    
    # find our starting cell
    for key, value in board.items():
        if 'r' in value:
            cell = key
    print(board.get(cell))
    
    # extracting coordinates from starting cell
    (r,q) = cell
    
    # making use of more manageable vector forms
    directions = vector_maker()
    
    # applying a vector on some cell
    #vector = directions['nw']
    #next_r = r + vector[0]
    #next_q = q + vector[1]  
    
    # accounting for infinite tiling
    #next_cell = bound_out(next_r, next_q)
    
    #print(next_cell)
    
    # building on above, try applying a spread move
    spread_move(board, r, q, board.get(cell[1]), 's')
    print(board)
    
    actions = [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]

    # Here we're returning "hardcoded" actions for the given test.csv file.
    # Of course, you'll need to replace this with an actual solution...
    return actions

# mini function to account for infinite board
def bound_out(r, q):
    if r > 6:
        r -= 7  
    if q > 6:
        q -= 7  
    if r < 0:
        r += 7  
    if q < 0:
        q += 7 
    return (r, q)   

# mini function to create vector dictionary to make moves more manageable
def vector_maker():
    directions = {
        'n' : (+1,-1), #/\
        'ne': (+1, 0), #/>
        'se': ( 0,+1), #\>
        's' : (-1,+1), #\/
        'sw': (-1, 0), #</
        'nw': ( 0,-1)  #<\
    }
    return directions

# function to handle the spread move   
def spread_move(board, r, q, stack, dir):
    directions = vector_maker()
    
    # 'kill' the cell we are spreading from
    key = (r,q)
    board.pop(key)
    
    
    
    print(board)
    #for i in range(1, stack):

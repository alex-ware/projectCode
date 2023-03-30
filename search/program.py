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
    #print(board[cell][1])
    
    # extracting coordinates from starting cell
    #(r,q) = cell
    
    # making use of more manageable vector forms
    #directions = vector_maker()
    
    # applying a vector on some cell
    #vector = directions['nw']
    #next_r = r + vector[0]
    #next_q = q + vector[1]  
    
    # accounting for infinite tiling
    #next_cell = bound_out(next_r, next_q)
    
    #print(next_cell)
    
    # building on above, try applying a spread move
    spread_move(board, cell, 's')
    print(board)
    spread_move(board, (3,1), 'se')
    print(board)
    spread_move(board, (3,2), 's')
    print(board)
    spread_move(board, (1,4), 'nw')
    print(board)
    spread_move(board, (1,3), 'nw')
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
def spread_move(board, cell, dir):
    directions = vector_maker()
    (r,q) = cell
    
    # height of stack at this cell we finna spread
    stack = board[cell][1]
    
    # 'kill' the cell we are spreading from
    board.pop(cell)
    
    # update the rest of board after spread
    for i in range(1, stack + 1):
        # navigate to the iᵗʰ cell of the spread
        vector = directions[dir]
        next_r = r + vector[0] * i
        next_q = q + vector[1] * i
        # make sure we adhere to infinite tiling 
        next_cell = bound_out(next_r, next_q)
        #print(next_cell)
        
        # updating the iᵗʰ cell of the spread in board representation
        # if the cell is unoccupied we spread over it
        if(next_cell not in board):
            board[next_cell] = ('r', 1)
        
        # if cell is occupied we spread on top of it
        else:
            this_stack = board[next_cell][1]
            if(this_stack == 6):
                # kill cell if stack becomes > 6 :(
                board.pop(next_cell)
            else:
                board[next_cell] = ('r', this_stack + 1)
                
    return board
                                    
        
        
            
        

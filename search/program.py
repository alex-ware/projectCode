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
    
    """
    # mimics correct solution of spreading on our own ver of board
    print(board)
    print(render_board(board, ansi=True))
    
    spread_move(board, cell, 's')
    print(board)
    print(render_board(board, ansi=True))
    
    spread_move(board, (3,1), 'se')
    print(board)
    print(render_board(board, ansi=True))
    
    spread_move(board, (3,2), 's')
    print(board)
    print(render_board(board, ansi=True))
    
    spread_move(board, (1,4), 'nw')
    print(board)
    print(render_board(board, ansi=True))
    
    spread_move(board, (1,3), 'nw')
    print(board)
    print(render_board(board, ansi=True))
    """
    print(render_board(board, ansi = True))
    loop_board_search(board, cell)
    #print(neighbour_same(board, (1,1), 'n'))
   
    
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

# just spreads across the board until everything is red                                
def loop_board_search(board, start_cell):
    (r, q) = start_cell
    dir = 'ne'
    
    i = 0
    j = 0
    while (j < 6):    
        stack = board[bound_out(r + i, q + j)][1]
        spread_move(board, bound_out(r + i, q + j), dir)
        i = i + stack
        print(render_board(board, ansi = True))
        dir = 'ne'
        if (i == 6):
            j += 1
            i = 0
            dir = 's'
    
    """        
    for i in range(0, 7):
        for j in range(0, 7):
            if((r + i > 6) and (q + j > 6)):
                spread_move(board, (r + i - 7, q + j - 7), 'ne')
            if((r + i > 6) and (q + j <= 6)):
                spread_move(board, (r + i - 7, q + j), 'ne')
            if((r + i <= 6) and (q + j > 6)):
                spread_move(board, (r + i, q + j - 7), 'ne')     
            else:
                spread_move(board, (r + i, q + j), 'ne')
            print(board)
            print(render_board(board, ansi=True))
    """

     
# function to check difference between a cell and its neighbour in direction 'dir'       
def neighbour_same(board, cell, dir):
    (r, q) = cell
    directions = vector_maker()
    vector = directions[dir]
    
    neighbour_r = r + vector[0]
    neighbour_q = q + vector[1]
    neighbour = bound_out(neighbour_r, neighbour_q)
    
    # neighbour cell is not occupied
    if(neighbour not in board):
        return 0
    
    # neighbour cell is same colour as subject cell    
    if(board[cell][0] == board[neighbour][0]):
        return 1
    
    # neighbour cell is different colour to subject cell
    else:
        return 0             
            
        

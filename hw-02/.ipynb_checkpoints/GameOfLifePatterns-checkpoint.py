import numpy as np

'''
Helper functions to create a 2D array representing an initial state for the Game Of Life.
Each of these functions adds a "pattern" to a specified location of the 2D array and in a specified orientation.
'''

def add_glider(grid,row,col,dir):
    '''
    Add a 3x3 "glider" pattern to the grid. 
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "glider" (options: 'SE', 'SW', 'NE', or 'NW')
    '''
    if dir == 'SE':
        grid[row:row+3,col:col+3] = np.array([[0,1,0],[0,0,1],[1,1,1]])
    elif dir == 'SW':
        grid[row:row+3,col:col+3] = np.array([[0,1,0],[1,0,0],[1,1,1]])
    elif dir == 'NE':
        grid[row:row+3,col:col+3] = np.array([[1,1,1],[0,0,1],[0,1,0]])
    elif dir == 'NW':
        grid[row:row+3,col:col+3] = np.array([[1,1,1],[1,0,0],[0,1,0]])
    return grid

def add_blinker(grid,row,col,dir):
    '''
    Add a 3x1 or 1x3 "blinker" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "blinker" (options: 'vertical' or 'horizontal')
    '''
    if (dir == 'vertical'):
        grid[row:row+3,col] = 1
    elif (dir == 'horizontal'):
        grid[row,col:col+3] = 1
    return grid

def add_beehive(grid,row,col,dir):
    '''
    Add a 4x3 or 3x4 "beehive" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "beehive" (options: 'vertical' or 'horizontal')
    '''
    if dir == 'vertical':
        grid[row:row+4,col:col+3] = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]]).T
    elif dir == 'horizontal':
        grid[row:row+3,col:col+4] = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]])
    return grid

def add_pentadecathalon(grid,row,col,dir):
    '''
    Add a 8x3 or 3x8 "pentadecathalon" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "pentadecathalon" (options: 'vertical' or 'horizontal')
    '''
    if(dir == 'vertical'):
        grid[row:row+8,col:col+3] = 1
        grid[row+1,col+1] = 0
        grid[row+6,col+1] = 0
    elif(dir == 'horizontal'):
        grid[row:row+3,col:col+8] = 1
        grid[row+1,col+1] = 0
        grid[row+1,col+6] = 0
    return grid

def add_spaceship(grid,row,col,dir):
    '''
    Add a 5x4 or 4x5 "spaceship" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "spaceship" (options: 'E', 'W', 'S', or 'N')
    '''
    if dir == 'E':
        grid[row:row+4,col:col+5] = np.array([[0,1,1,1,1],[1,0,0,0,1],[0,0,0,0,1],[1,0,0,1,0]])
    elif dir == 'W':
        grid[row:row+4,col:col+5] = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[0,1,0,0,1]])
    elif dir == 'S':
        grid[row:row+5,col:col+4] = np.array([[0,1,1,1,1],[1,0,0,0,1],[0,0,0,0,1],[1,0,0,1,0]]).T
    elif dir == 'N':
        grid[row:row+5,col:col+4] = np.array([[1,1,1,1,0],[1,0,0,0,1],[1,0,0,0,0],[0,1,0,0,1]]).T
    return grid

def add_generator(grid,row,col,dir):
    '''
    Add a 9x37 "generator" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "generator" (options: 'SE', 'SW', 'NE', or 'NW')
    '''
    A = np.zeros((9,37))
    A[4:6,0:2] = 1
    A[4:7,[10,16]] = 1
    A[3,[11,15]] = 1
    A[7,[11,15]] = 1
    A[[2,8],12:14] = 1
    A[5,[14,17]] = 1
    A[2:5,20:22] = 1
    A[[1,5],22] = 1
    A[[0,1,5,6],24] = 1    
    A[2:4,34:36] = 1
    if dir == 'SE':
        grid[row:row+9,col:col+37] = A
    elif dir == 'SW':
        grid[row:row+9,col:col+37] = A[:,::-1]
    elif dir == 'NE':
        grid[row:row+9,col:col+37] = A[::-1,:]
    elif dir == 'NW':
        grid[row:row+9,col:col+37] = A[::-1,::-1]
    return grid

def add_diehard(grid,row,col,dir):
    '''
    Add a 3x8 or 8x3 "diehard" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "diehard" (options: 'N', 'E', 'S', or 'W')
    '''
    A = np.zeros((3,8))
    A[1:3,0:2] = np.array([[1,1],[0,1]])
    A[0,6] = 1
    A[2,5:8] = 1
    if dir == 'N':
        grid[row:row+3,col:col+8] = A
    elif dir == 'E':
        grid[row:row+8,col:col+3] = A.T
    elif dir == 'S':
        grid[row:row+3,col:col+8] = A[::-1,:]
    elif dir == 'W':
        grid[row:row+8,col:col+3] = A[::-1,:].T
    return grid

def add_R(grid,row,col,dir):
    '''
    Add a 3x3 "R" pattern to the grid
    (row,col) specifies the location of the top-left corner
    dir specifies the orientation of the "R" (options: 'N', 'E', 'S', or 'W')
    '''
    if dir == 'N':
        grid[row:row+3,col:col+3] = np.array([[0,1,1],[1,1,0],[0,1,0]])
    elif dir == 'E':
        grid[row:row+3,col:col+3] = np.array([[0,1,1],[1,1,0],[0,1,0]]).T
    elif dir == 'S':
        grid[row:row+3,col:col+3] = np.array([[0,1,0],[1,1,0],[0,1,1]])
    elif dir == 'W':
        grid[row:row+3,col:col+3] = np.array([[0,1,0],[1,1,0],[0,1,1]]).T
    return grid
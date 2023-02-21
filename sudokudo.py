
import numpy as np

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

# Scan the puzzle to determine equations 
equations = []
sudoku_vars = 0

# From left to right...
for i in range(9):
    
    const = 45
    equ_vars = []
    for j in range(9):
        
        # If selection is an int...
        if isinstance(puzzle[i][j], int):
            
            # And greater than zero, that means it is a constant
            if puzzle[i][j] > 0: 
                const -= puzzle[i][j]
            
            # If it's zero, that means it is a new variable. So, increasing 
            # Variables' number and saving a new string to determine it in future
            else:
                sudoku_vars += 1
                puzzle[i][j] = str(sudoku_vars)
        
        # If selection is a str, so variable, save it to equation variables. Keep in mind that this step 
        # can still run after checking for int values. 
        if isinstance(puzzle[i][j], str):
            equ_vars.append(puzzle[i][j])
            
    equations.append((equ_vars, const))
        
# And top to bottom...
for j in range(9):
    
    const = 45
    equ_vars = []
    for i in range(9):
        
        if isinstance(puzzle[i][j], int):
                const -= puzzle[i][j]
        else:
            equ_vars.append(puzzle[i][j])
            
    equations.append((equ_vars, const))
 
# And finally, blocks.
# Using 3x3 indexing for locating blocks. And using i/j indexing later
for block_i in range(3):
    for block_j in range(3):
        
        const = 45
        equ_vars = []
        for i in range(block_i * 3, block_i * 3 + 3):
            for j in range(block_j * 3, block_j * 3 + 3):
                
                if isinstance(puzzle[i][j], int):
                        const -= puzzle[i][j]
                else:
                    equ_vars.append(puzzle[i][j])
                    
        equations.append((equ_vars, const))

# Now get the results using a lineer algebric equations system. A.X = b
# For these, creating some 2D arrays (matrixes)...
A = np.zeros((len(equations), sudoku_vars), dtype=int)
b = np.zeros((len(equations), 1), dtype=int)

# And then populating them with equation values
i = 0
for equ_vars, const in equations:
    
    for v in equ_vars:
        A[i][int(v) - 1] = 1
    b[i] = const
    
    i += 1


 
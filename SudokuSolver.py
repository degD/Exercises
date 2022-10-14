
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# TODO: RE-DO!!!

def sudoku_solver_1(puzzle):
    """Solves sudoku using a brute-force approach. 
    Solves from left-to-right and top-to-bottom.
    
    It takes a 9x9 unsolved sudoku and returns it's result."""
    
    # Algorithm definitions
    oldval = x = y = 0
    past_coords = []

    # Main loop
    while y < 9:
        
        if puzzle[y][x] == 0:
            
            row = puzzle[y]
            col = [puzzle[i][x] for i in range(9)]
            
            for num in range(oldval+1, 10):
                if (num not in row) and (num not in col):
                    puzzle[y][x] = num
                    break
            
            if puzzle[y][x]:
                oldval = 0
                past_coords.append((y, x))
            
            else:
                y, x = past_coords.pop()
                oldval = puzzle[y][x]
                puzzle[y][x] = 0
                continue
        
        # Movement algorithm     
        if x < 8:
            x += 1
        else:
            y += 1
            x = 0
        
    return puzzle

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

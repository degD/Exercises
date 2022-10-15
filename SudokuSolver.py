
import random as rd

def SudokuSolver(puzzle):
    """Solves the given 9x9 sudoku and returns the result. 
    Returns 0 if the sudoku is unsolvable"""
    
    def square_index(y, x):
        return (x // 3) + (y // 3)*3

    # Defining some values prior to start
    puzzle_3x3_data = [list() for _ in range(9)]
    puzzle_columns = [list() for _ in range(9)]
    puzzle_unk = []

    for y in range(9):
        for x in range(9):
            
            sqi = square_index(y, x)
            puzzle_3x3_data[sqi].append(puzzle[y][x])
            puzzle_columns[x].append(puzzle[y][x])
            
            if puzzle[y][x] == 0:
                puzzle_unk.append((y, x))
            
    # Some variables for the main algorithm loop
    x = y = 0
    init_val = 0
    past_coords = []

    # Main algorithm loop
    while y < 9:
        
        if puzzle[y][x] == 0:
            
            sqi = square_index(y, x)
            
            squ_list = puzzle_3x3_data[sqi]
            col_list = puzzle_columns[x]
            row_list = puzzle[y]
            
            for num in range(init_val+1, 10):
                if (num not in squ_list) and (num not in col_list) and (num not in row_list):
                    puzzle[y][x] = num
                    break
                
            if puzzle[y][x]:
                squ_list.remove(0)
                squ_list.append(num)
                col_list[y] = num
                puzzle_unk.remove((y, x))
                
                init_val = 0
                past_coords.append((y, x))
                
            else:
                try:
                    y, x = past_coords.pop()
                except IndexError:
                    return 0
                init_val = puzzle[y][x]
                puzzle[y][x] = 0

                sqi = square_index(y, x)
                squ_list = puzzle_3x3_data[sqi]
                squ_list.remove(init_val)
                squ_list.append(0)
                col_list = puzzle_columns[x]
                col_list[y] = 0
                puzzle_unk.append((y, x))
                
                continue
    
    # Movement unit. Change it to alter how coordinates are changed.
        try:
            y, x = rd.choice(puzzle_unk)
        except IndexError:
            return puzzle
            
    return puzzle
        
# HOW IT WORKS:
# Iterates over each coordinate as defined by movement unit. And if it's 0, then 
# tries to find a number between 1-9, that doesn't exist in its row, column,
# and 3x3 square. If this number exists, algorithm skips to next coordinate. Else, 
# goes to the former numerated coordinate, and tries to find another value for it.
# The code exits when Sudoku gets completed or it finds out it is impossible to complete it.



if __name__ == '__main__':
    
    import time
    
    puzzle1 = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    solution1 = [[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],
                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],
                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]]
    
    puzzle2 = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
               [0, 0, 0, 4, 0, 6, 0, 0, 0],
               [0, 0, 5, 0, 7, 0, 3, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 4, 0],
               [4, 0, 1, 0, 6, 0, 5, 0, 8],
               [0, 9, 0, 0, 0, 0, 0, 2, 0],
               [0, 0, 7, 0, 3, 0, 2, 0, 0],
               [0, 0, 0, 7, 0, 5, 0, 0, 0],
               [1, 0, 0, 0, 4, 0, 0, 0, 7]]
    
    solution2 = [[9, 2, 6, 5, 8, 3, 4, 7, 1],
                 [7, 1, 3, 4, 2, 6, 9, 8, 5],
                 [8, 4, 5, 9, 7, 1, 3, 6, 2],
                 [3, 6, 2, 8, 5, 7, 1, 4, 9],
                 [4, 7, 1, 2, 6, 9, 5, 3, 8],
                 [5, 9, 8, 3, 1, 4, 7, 2, 6],
                 [6, 5, 7, 1, 3, 8, 2, 9, 4],
                 [2, 8, 4, 7, 9, 5, 6, 1, 3],
                 [1, 3, 9, 6, 4, 2, 8, 5, 7]]
    
# First test
    start = time.perf_counter()
    result1 = SudokuSolver(puzzle1)
    stop = time.perf_counter()
    
    time_ms = int(round(stop-start, 3)*1000)
    if result1 == solution1:
        print(f'Sudoku solved! ({time_ms}ms)')
    else:
        print('Something went wrong...')

# Second, harder test
    start = time.perf_counter()
    result2 = SudokuSolver(puzzle2)
    stop = time.perf_counter()
    
    time_ms = int(round(stop-start, 3)*1000)
    if result2 == solution2:
        print(f'Sudoku solved! ({time_ms}ms)')
    else:
        print('Something went wrong...')

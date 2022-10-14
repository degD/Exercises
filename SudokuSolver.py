
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def square_index(y, x):
   return (x // 3) + (y // 3)*3

# Defining some values prior to start
puzzle_3x3_data = [list() for _ in range(9)]
puzzle_columns = [list() for _ in range(9)]

for y in range(9):
    for x in range(9):
        
        sqi = square_index(y, x)
        puzzle_3x3_data[sqi].append(puzzle[y][x])
        puzzle_columns[x].append(puzzle[y][x])
        
# Main algorithm loop
x = y = 0
init_val = 0
past_coords = []

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
            
            init_val = 0
            past_coords.append((y, x))
            
        else:
            y, x = past_coords.pop()
            init_val = puzzle[y][x]
            puzzle[y][x] = 0

            sqi = square_index(y, x)
            squ_list = puzzle_3x3_data[sqi]
            squ_list.remove(init_val)
            squ_list.append(0)
            col_list = puzzle_columns[x]
            col_list[y] = 0
            
            continue
        
    if x < 8:
        x += 1
    else:
        x = 0
        y += 1

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

if puzzle == solution:
    print('YEAH!') 
else:
    print(puzzle)
            
            
        
        
        
        



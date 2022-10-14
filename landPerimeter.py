
def land_perimeter(arr):
    """
    Function for calculating land perimeter from a 2-dimensional list
    of 'X' and '0'.
    Assumes arr is an 2-dimensional array of 'X' and '0'.
    Returns the land perimeter by 'X'.
    """
    
    peri = 0

    len_y = len(arr)
    len_x = len(arr[0])
    len_total = len_y * len_x
    
    for i in range(len_total):
        y = i // len_x
        x = i % len_x
        
        if arr[y][x] == 'X':
            peri += 4
            
            try:
                if arr[y][x+1] == 'X':
                    peri -= 2
            except IndexError:
                pass
            
            try:
                if arr[y+1][x] == 'X':
                    peri -= 2
            except IndexError:
                pass
                
    return 'Total land perimeter: ' + str(peri)

if __name__ == '__main__':
    print('TEST:')
    res = land_perimeter(["OXOO", 
                          "OXOX"])
    print(res)

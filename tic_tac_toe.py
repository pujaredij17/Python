def tic_tac_toe(grid):
    for i in range(0,3):
        row = set ([grid[i][0],grid[i][1],grid[i][2]])
        if (len(row) == 1 and grid [i][0] != 0 ):
            return grid[i][0]
        
    for j in range(0,3):
        column = set ([grid[0][j],grid[1][j], grid[2][j]])
        if (len(column) == 1 and grid [0][j] != 0):
            return grid [0][j]
        
    for k in range(0,3):
        diag1 = set ([grid [0][0], grid [1][1], grid [2][2]])
        diag2 = set ([grid [0][2], grid [1][1], grid [2][0]])
        
        if len(diag1) == 1 or len(diag2) == 1 and grid [1][1] != 0 :
            return grid [1][1]
     
        
if __name__ == "__main__":
    
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]
    
    result = tic_tac_toe(also_no_winner)
    print(result)
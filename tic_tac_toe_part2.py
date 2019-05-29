gameboard = [(['.']*3) for i in range(3)]
player = 1
#print(gameboard)
def draw_board(row_col, piece):
    if gameboard[int(row_col[0])][int(row_col[1])] == '.' :
        gameboard[int(row_col[0])][int(row_col[1])] = piece
    
    else:
        print("position already taken")
        exit(0)
    
    for element in gameboard:
        print(element)   
"""        
def draw(width, height):
    draw_line(width, " ", "__")
    for i in range(height):
        draw_line(width, "|", "__")
    print("\n")    
"""        
     
   
def tic_tac_toe():
            
    for i in range(0,3):
        row = set ([gameboard[i][0],gameboard[i][1],gameboard[i][2]])
        if (len(row) == 1 and gameboard [i][0] == 'X' ):
            print("Player1 wins")
            print("1")
            return 1

            
        elif (len(row) == 1 and gameboard [i][0] == 'O' ):
            print("Player2 wins")
            print("2")
            return 1
        
    for j in range(0,3):
        column = set ([gameboard[0][j],gameboard[1][j], gameboard[2][j]])
        if (len(column) == 1 and gameboard [0][j] == 'X'):
            print("Player1 wins")
            print("3")
            return 1
            
        elif (len(row) == 1 and gameboard [i][0] == 'O' ):
            print("Player2 wins")
            print("4")
            return 1
        
    diag1 = set ([gameboard [0][0], gameboard [1][1], gameboard [2][2]])
    diag2 = set ([gameboard [0][2], gameboard [1][1], gameboard [2][0]])
        
    if ((len(diag1) == 1 or len(diag2) == 1) and gameboard [1][1] == 'X') :
        print("Player1 wins")
        print("5")
        return 1


    if ((len(diag1) == 1 or len(diag2) == 1) and gameboard [1][1] == 'O') :
        print("Player2 wins")
        print("6")
        return 1

            
    for sublist in gameboard:
        if '.' in sublist:
            return 0      
        
    print("Game Over")
    return 1

        
if __name__ == "__main__":
    
    while not tic_tac_toe():
        if player == 1:
            piece = 'X'
    
        elif player == 2:
            piece = 'O'    
        
        p1  = input("Player" + str(player) + "input:")
        row_col = p1.split(",")     
     
        draw_board(row_col, piece)  
        if (player == 1):
            player = 2
        else:
            player = 1      
            
        #draw(3,3)        
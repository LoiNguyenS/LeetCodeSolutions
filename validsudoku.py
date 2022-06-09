
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for row in range(9):
        for column in range(9):
            if board[row][column] != ".": #if the element we are checking is equal to ".", we check
                for n in range(1,10): #between 1 to 9 , range is non-inclusive
                        #checks if the number will work in the row, column and nonet
                        #checks row
                        for i in range(0,9):
                            if board[row][i] == n:
                                return False

                        #checks column
                        for i in range(0,9):
                            if board[i][column] == n:
                                return False    

                        #for the nonet        
                        x0 = (column//3)*3 #column
                        y0 = (row//3)*3 #row

                        #CHECKS nONET
                        for i in range(0,3):
                             for j in range(0,3):
                                if board[y0+i][x0+j] == n:  #a_list[row][col]
                                    return False        
    return True



    grid1 = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    
    if isValidSudoku(grid1) == True:
        print("True")
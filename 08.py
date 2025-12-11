board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
def horizont():
    for i in range(9):
        for j in range(9):
            for h in range(9):
                if board[i][h] == board[i][j] and board[i][h] != "." and board[i][j] != "." and h != j:
                    return False
    return True

def vert():
    rang1 = range(3)
    rang2 = range(3, 6)
    rang3 = range(6, 9)
    for i in range(9):
        for j in range(1, 9):
            for k in range(9):
                for h in range(9):
                    if board[i][h] == board[j][k] and board[j][k] != "." and board[i][h] != "." and k == h and i != j:
                        return False
                    elif (board[i][h] == board[j][k] and board[j][k] != "." and board[i][h] != "." and i != j) and ((k in rang1 and h in rang1) or (k in rang2 and h in rang2) or (k in rang3 and h in rang3)) and ((j in rang1 and i in rang1) or (j in rang2 and i in rang2) or (j in rang3 and i in rang3)):
                        return False
    return True


def main():
    if horizont() and vert():
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(main())
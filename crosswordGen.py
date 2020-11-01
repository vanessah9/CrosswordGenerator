rows = 20
col = 20
blank = '.'
board = [[blank] * col for i in range(rows)]
global boardLength
boardLength = len(board)

def printBoard(board):

    def count():
        print(" ", end="")
        for i in range(2):
            for j in range(10):
                print(j, end="")
        print()
    count()

    def horizontalBorder():
        print(" ", end="")
        for i in range(rows):
            print("_", end="")
        print()
    horizontalBorder()

    for i in range(rows):
        print('|', end='')
        for j in range(col):
            if board[i][j] == " ":
                print(".", end="")
            else:
                print(board[i][j], end="")
        print('|' + str(i), end='')
        print()

    horizontalBorder()
    count()

# printBoard(board)

def addFirstWord(board, word):

    middle = boardLength//2
    validWord = True
    if len(word) > rows or len(word) + 1 > rows:
        validWord = False
    if validWord:
        for i in range(len(word)):
            board[middle][i+1] = word[i]

def checkvertical(board, word, row, col) :
    D = len(board)
    n = len(word)
    blank = ' '

    #Checks if word fits entirely on board
    if n + row > 20 :

        print(word, 'is too long to fit going down starting at row', row )

        return False

    #Checks for empty letter/intersecting letter
    for k in range(n) :

        if board[row + k][col] != '.' and board[row + k][col] != word[k]:
            return False

    return True

def matchingletter(board,word):
    for i in board[10]:
        if str(i) in word:
            position = word.index(i)
            print(i)
            print(position)
matchingletter(board,"cat")

def find(board, letter) :
    D = len(board)
    for i in range(D) :
        for j in range(D) :
            if board[i][j] == letter:
                return (i, j)
    return None
addFirstWord(board, "hippopotamus")
# printBoard(board)

(pos_y, pos_x) = find(board, 'a')

def addvertical(board, word) :
    notFound = True
    # go across and down the whole board looking for a spot to add word
    # (pos_y, pos_x) = find(board, 'a')
    # print(pos_y, pos_x)
    row = int
    col = int
    for i in range(len(board)) :
        for j in range(len(board)) :
            # check if word can go at (i,j)  and if it can, then place it there
            for x in range (len(word)):
                if notFound:
                    if board[i + x][j] == word[x]:
                        if checkvertical(board, word, i, j):
                            notFound = False
                            row = i
                            col = j

    for x in range(len(word)):
        board[row + x][col] = word[x]

    printBoard(board)


addvertical(board, 'horse')

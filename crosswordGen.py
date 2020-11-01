rows = 20
col = 20
blank = '.'
board = [[blank] * col for i in range(rows)]


def print_board(board):
    """ This function prints the board along with a coordinate system
on the sides using a count function """

    def count():
        print("", end="")

        for i in range(2):

            for j in range(10):
                print(j, end=" ")

        print()

    count()

    for i in range(rows):

        for j in range(col):

            if board[i][j] == " ":
                print(".", end=" ")

            else:
                print(board[i][j], end=" ")
        print(str(i), end='')
        print()

    count()


# def add_firstword(board, word):
#     if len(word) > rows:
#         return False
#     return True


def check_vertical(board, word, row, col):
    """ A function that returns True if the word can be added to the board starting at
      position board[row][col] and going vertically. """

    n = len(word)

    # Checks if word fits entirely on board
    if n + row > 20:
        return False

    # Checks for empty letter/intersecting letter
    for k in range(n):

        if board[row + k][col] == word[k]:
            if board[row + k + 1][col] != ".":
                # print('reached case 9 at word ' + word)
                return False
            pass

        # checks the beginning of the word
        if k == 0:
            if board[row - 1][col] != "." or board[row][col + 1] != "." or board[row][col - 1] != ".":
                # print('reached case 5 at word ' + word)
                # print('reached case 5 at word ' + word + ' at position ' + str(row) + ', ' + str(col))
                return False

        # checks the end of the word
        if k == n - 1:
            if board[row + 1][col] != "." or board[row][col + 1] != "." or board[row][col - 1]  != ".":
                # print('reached case 6 at word ' + word)
                return False

        # checks in between the beginning and end
        if 0 < k < n:
            if board[row][col + 1] != "." and board[row][col - 1]  != ".":
                # print('reached case 7 at word ' + word)
                # print('reached case 7 at word ' + word + ' at position ' + str(row) + ', ' + str(col))
                return False

        if board[row + k][col] != '.' and board[row + k][col] != word[k]:
            return False


    return True


def add_vertical(board, word):
    notFound = True
    # go across and down the whole board looking for a spot to add word

    row = int
    col = int

    for y_pos in range(len(board)):

        for x_pos in range(len(board)):

            # check if word can go at (i,j)  and if it can, then place it there
            for i in range(len(word)):

                if notFound:

                    if y_pos + i >= 20:
                        notFound = True

                    elif board[y_pos + i][x_pos] == word[i]:

                        if check_vertical(board, word, y_pos, x_pos):
                            notFound = False
                            row = y_pos
                            col = x_pos

    if notFound:
        print(word + ' could not be placed vertically')
        # print(L)
        L.append(word)
        # print(L)
    else:
        print(word, "is placed vertically at", "(", col, ",", row, ")")
        for x in range(len(word)):
            board[row + x][col] = word[x]


def check_horizontal(board, word, row, col):
    """ This function returns True if the word can be added to the board starting at
    position board[row][col] and going horizontally. """
    n = len(word)

    # Checks if word fits entirely on board
    if n + col > 20:
        return False

    for k in range(n):

        if board[row][col + k] == word[k]:
            if board[row][col + k + 1] != ".":
                # print('reached case 8 at word ' + word)
                return False
            pass

        if k == 0:
            if board[row][col - 1] != "." or board[row + 1][col] != "." or board[row - 1][col] != ".":
                # print('reached case 1 at word ' + word)
                return False


        if k == n-1:
            if board[row + 1][col] != "." or board[row][col + 1] != "." or board[row][col - 1] != ".":
                # print('reached case 2 at word ' + word)
                return False

        if 0 < k < n:
            if board[row + 1][col] != "." and board[row - 1][col] != ".":
                # print('reached case 3 at word ' + word + ' at position ' + str(row) + ', ' + str(col))
                return False

        if board[row][col + k] != '.' and board[row][col + k] != word[k]:
            # print('reached case 4 at word ' + word)
            return False

    return True


def add_horizontal(board, word):
    """ This function adds the word horizontally. It goes through the entire board
    and finds a valid spot using check_horizontal function. If notFound is false it will
    place the word by keeping the row position the same and increment the column position.
    Otherwise, if notFound is true then the word will be added to the end of the list. """

    notFound = True


    row = int
    col = int

    # go across and down the whole board looking for a spot to add word
    # iterates through each row and checks each element
    for y_pos in range(len(board)):

        for x_pos in range(len(board)):

            # check if word can go at (y_pos, x_pos)  and if it can, then place it there
            for i in range(len(word)):

                if notFound:

                    # checks if the word at position x_pos goes out of bounds
                    if x_pos + i >= 20:
                        notFound = True

                    elif board[y_pos][x_pos + i] == word[i]:

                        # if check_horizontal function returns True, that means it can be added horizontally
                        if check_horizontal(board, word, y_pos, x_pos):
                            notFound = False
                            row = y_pos
                            col = x_pos

    if notFound:
        print(word + ' could not be placed horizontally')
        # print(L)
        L.append(word)
        # print(L)

    else:
        print(word, "is placed horizontally at", "(", col, ",", row, ")")
        for x in range(len(word)):
            board[row][col + x] = word[x]


# L = ['hippopotamus', 'horse', 'loon', 'snake', 'cat', 'rattlesnake', 'dinosaur']
L = ['addle', 'apple', 'loop', 'aim', 'pool', 'baim', 'pat']
# L = ["hi" for i in range(50)]
# L = ['clowning', 'apple', 'addle',  'incline', 'plan', 'burr' ]
# L = ['abcdefghijklmnopqrstuvwxyz']
# L = ['addle', 'apple', 'rainy', 'nasty', 'plan', 'burr']
# L = ['homesick', 'here', 'room', 'off', 'fun', 'until', 'glass']
# L = ["abcdefghijklmnopqrst", "fffffggg", "ttttttttttuuuuuuuuuz", "yzzz", "qqqqqqqqqqqqqqy","xxxxxxxxxaaaaaaa", "aaaaggg", "xxwwww","wwwwvvvvve", "vvvvvvvvvvvvq", "mat", "mat",
#                "make", "make", "maker", "remake", "hat", ]


def add_words(board, L):

    # if add_firstword(board, L[0]):

    # this adds the first word of the list to the center of the board

    row_midpoint = rows//2
    col_midpoint = col//2
    word_midpoint = len(L[0]) // 2

    # for loop starts from 2nd item in the list
    # if the item index is even, it prints horizontally and if it is odd then it prints vertically
    for i in range(0, len(L)):

        if i == 0:
            print(L[0], "is placed horizontally at", "(", col_midpoint - (word_midpoint), ", 10 )")
            for i in range(len(L[0])):
                board[row_midpoint][col_midpoint - (word_midpoint) + i] = L[0][i]
            # print_board(board)
            print()

        elif i % 2 == 0:
            add_horizontal(board, L[i])
            # print_board(board)
            print()

        elif i % 2 != 0:
            add_vertical(board, L[i])
            # print_board(board)
            print()

add_words(board, L)
print_board(board)

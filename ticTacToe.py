
dimension = 0
board = []
indices = []
turn = 0

def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        global board
        board = []
        global turn
        turn = 0
        k = input("What would you like the dimensions of the board to be? ").strip()
        while True:
            try:
                k = int(k)
                if (k < 3 or k > 10):
                    raise RuntimeError("invalid number")
                break
            except:
                print()
                print("please enter a number between 3 and 10 inclusive")
                k = input("What would you like the dimensions of the board to be? ").strip()
        global dimension
        dimension = k
        print("Your board will be a " + str(dimension) + "x" + str(dimension) + " board\n")
        createBoard()
        while not winningState() and turn < (dimension * dimension):
            if turn % 2 == 0:
                print("Player 1's turn")
            else:
                print("Player 2's turn")
            print("Current board state:")
            boardToString()
            move()
            turn += 1
        boardToString()
        print()
        if winningState():
            print("Player " + str(((turn + 1) % 2) + 1) + " wins!")
        else:
            print("Stalemate")
        k = input("Press 1 to play again, or anything else to quit: ").strip()
        if (k != '1'):
            break



def createBoard():
    global board
    global indices
    indices = list(range(dimension))
    for i in indices:
        temp = []
        for j in indices:
            temp.append("+")
        board.append(temp)

def boardToString():
    counter = 0
    s = "   "
    for i in indices:
        s += str(i) + "   "
    print(s)
    for i in board:
        p = str(counter) + "| "
        for j in i:
            p += j + " | "
        print(p[:len(p) - 2])
        if not(i is board[len(board) - 1]):
            print( "  " + ("-" * (len(p) - 4)))
        counter += 1

def drop(xpos,ypos,char):
    global board
    if (board[xpos][ypos] != '+'):
        raise RuntimeError("that square is already filled")
    board[xpos][ypos] = char

def move():
    todrop = ''
    global turn
    if (turn % 2 == 0):
        todrop = 'X'
    else:
        todrop = 'O'
    while True:
        try:
            k = input("Enter the coordinates of your move with horizontal coordinate first, separated by spaces: ").strip()
            l = k.split()
            if len(l) != 2:
                print("Please enter exactly two coordinates")
                raise RuntimeError("more than 2 coordinates")
            x = int(l[0])
            y = int(l[1])
            if x not in indices or y not in indices:
                raise RuntimeError("Invalid indices")
            drop(y,x,todrop)
            break
        except:
            print("Invalid move, please redo it")
    print()


def winningState():
    return horizontalVictory() or verticalVictory() or dDiagVictory() or uDiagVictory()

def horizontalVictory():
    for i in board:
        if (checkHrow(i)):
            return True
    return False

def checkHrow(row):
    if row[0] == '+':
        return False
    for j in indices[1:]:
        if row[j] != row[j-1]:
            return False
    return True

def verticalVictory():
    for i in indices:
        if checkCol(i):
            return True
    return False

def checkCol(index):
    if board[0][index] == '+':
        return False
    for j in indices[1:]:
        if board[j][index] != board[j-1][index]:
            return False
    return True

def dDiagVictory():
    if board[0][0] == '+':
        return False
    for j in indices[1:]:
        if board[j-1][j-1] != board[j][j]:
            return False
    return True

def uDiagVictory():
    if board[0][dimension - 1] == '+':
        return False
    for j in indices[1:]:
        if board[j-1][dimension - j] != board[j][dimension - 1 - j]:
            return False
    return True

from operator import index
import sys
from collections import deque

stack = deque()

#Reads sudoku puzzle from file and returns a 2d list of integers with the values in it
def parseInput(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Input file does not exist")
        sys.exit(0) #exits the program if the file does not exist
    content = file.read()
    file.close()

    #Replaces all the blank tiles with 0 for computation later on
    content = content.replace(" ", "0")

    #Creates a new string list without "|" and newline symbol
    strList = [e for e in content if e not in ('|', '\n')]

    #Converts the list of strings to a 2d list of integers
    intList = list(map(int, strList))
    list2d = [[intList[(j * 9) + i] for i in range(9)] for j in range(9)]
    return list2d

#Writes the solved puzzle into an output file called output.txt
def outputToFile(board):
    try:
        file = open("output.txt", "x")
    except FileExistsError:
        pass #Ignores error if file already exists
    finally:
        file = open("output.txt", "w")
    
    #Build the ouput string to be written into the file
    output = ""
    for i in range(9):
        for j in range(9):
            output += "|" + str(board[i][j]) + "|"
        if i != 8:
            output += "\n"
    file.write(output)

#Checks if the sudoku puzzle is solved by checking that there are no tiles with 0
#Returns true if it is solved
def isSolved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

#Prints board for debugging purpose
def printBoard(board):
    output = ""
    for i in range(9):
        for j in range(9):
            output += "|" + str(board[i][j]) + "|"
        output += "\n"
    print(output)

#Checks if any constraints are violated for that tile
#Returns true if it does not violate
def checkConstraints(board, val, row, col):
    #Check rows
    for i in range(9):
        if i == col:
            continue
        elif(val == board[row][i]):
            return False

	#Check columns
    for i in range(9):
        if i == row:
            continue
        elif(val == board[i][col]):
            return False

    #Check subgrid
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            tempRow = startRow + i
            tempCol = startCol + j
            if(tempRow == row and tempCol == col):
                continue
            elif(val == board[tempRow][tempCol]):
                return False

    return True

#Returns the unique index of the first blank tile found
#Equation of index = row*9 + column
def getBlankTiles(board):
    listOfBlankTiles = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                listOfBlankTiles.append(i*9 + j)
    print(listOfBlankTiles)
    return listOfBlankTiles


board = parseInput("input.txt")
startSolver(board)
print(isSolved(board))
printBoard(board)
#outputToFile(board)

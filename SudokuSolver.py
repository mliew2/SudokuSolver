from operator import index
import sys

board = []

def parseInput(filename):
    """
    Reads sudoku puzzle from 'filename'
    Returns a 2d list of integers representing the puzzle
    """
    try:
        file = open(filename, "r")

    #exits the program if the file does not exist
    except FileNotFoundError:
        print("Input file does not exist")
        sys.exit(0)

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


def outputToFile():
    """
    Writes the solved puzzle into an output file called output.txt
    Only called when puzzle is solved
    """
    #Creates the file output.txt if it does not exist
    try:
        file = open("output.txt", "x")

    #Ignores error if file already exists
    except FileExistsError:
        pass
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


def isSolved():
    """
    Checks if the sudoku puzzle is solved by checking that there are no tiles with 0
    Returns true if it is solved
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def printBoard():
    """
    Prints the current state of the board 
    Mostly for debugging purpose
    """
    output = ""
    for i in range(9):
        for j in range(9):
            output += "|" + str(board[i][j]) + "|"
        output += "\n"
    print(output)


def checkConstraints(val, row, col):
    """
    Consistency checks to see if inserting the 'val' at board[row][col] will result in a violation
    That is the value does not appear in the same row, column and 3x3 subgrid
    Returns true if it does not violate
    """
    #Check rows
    for i in range(9):
        if i == col:
            continue
        elif val == board[row][i]:
            return False

	#Check columns
    for i in range(9):
        if i == row:
            continue
        elif val == board[i][col]:
            return False

    #Check subgrid
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        tempRow = startRow + i
        for j in range(3):
            tempCol = startCol + j
            if tempRow == row and tempCol == col:
                continue
            elif val == board[tempRow][tempCol]:
                return False

    return True


def getBlankTiles():
    """
    Returns a list of unique indices of the blank tiles on the board
    Equation to get unique index = row*9 + column
    """
    listOfBlankTiles = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                listOfBlankTiles.append(i*9 + j)
    return listOfBlankTiles


def backtrack(count, blankTiles):
    """
    Does a depth-first search recustively to find a solution to the puzzle
    'count' is used to get the next blank tile index from the 'blankTiles' list
    """
    #Base case to check if the puzzle is solved and returns True if solved
    if isSolved():
        return True
    else:
        index = blankTiles[count]
        for i in range(1, 10):

            #If all 1-9 violates the constraints for the current tile
            #return false to leave this branch and try a different branch
            if i == 9 and not checkConstraints(i, index//9, index%9):
                return False

            #Constraints are checked every time before a value is inserted into the board
            elif not checkConstraints(i, index//9, index%9):
                continue

            #If the constraints are not violated, insert value into that tile
            #then moves on to search the next blank tile
            else:
                board[index//9][index%9] = i
                if backtrack(count+1, blankTiles):
                    return True
                
                #Reassign that tile to 0 if the current branch is not a path to the solution
                else:
                    board[index//9][index%9] = 0


def startSolver():
    """
    Starts the algorithm to solve the Sudoku puzzle
    Calles the outputToFile function if a solution is found
    Prints a message otherwise
    """
    blankTiles = getBlankTiles()
    if backtrack(0, blankTiles):
        outputToFile()
    else:
        print("No solution found. This is not a valid Sudoku")


board = parseInput("test.txt")
startSolver()

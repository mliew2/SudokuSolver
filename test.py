import sys

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
    board = [[intList[(j * 9) + i] for i in range(9)] for j in range(9)]
    return board

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

#Prints board for debugging purpose
def printBoard(board):
    output = ""
    for i in range(9):
        for j in range(9):
            output += "|" + str(board[i][j]) + "|"
        output += "\n"
    print(output)


board = parseInput("input.txt")
printBoard(board)
#outputToFile(board)

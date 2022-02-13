import sys

#Read sudoku puzzle from file and return a list with the values in it
def parseInput(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Input file does not exist")
        sys.exit(0)
    content = file.read()
    file.close()

    #Replacing all the blank tiles with 0 for computation later on
    content = content.replace(" ", "0")

    #Create a new list without "|" and newline symbol
    board = [e for e in content if e not in ('|', '\n')]

    #returns a list of integers of the sudoku puzzle
    return list(map(int, board))

#Write the solved puzzle into an output file called output.txt
def outputToFile(board):
    try:
        file = open("output.txt", "x")
    except FileExistsError:
        pass
    finally:
        file = open("output.txt", "w")
    
    #Build the ouput string to be written into the file
    output = ""
    for i in range(9):
        for j in range(9):
            output += "|" + str(board[(i * 9) + j]) + "|"
        if i != 8:
            output += "\n"
    file.write(output)
    print (output)


board = parseInput("input.txt")
print(board)
print(len(board))
outputToFile(board)

import random


def create_board():
    battleBoard = []
    while True:
        try: 
            gridSize = int(input("Enter the size of your board. (Ex. 1-10): "))
            break
        except(ValueError):
            print ("Invalid input, try again.")

    for row in range(gridSize):
        board_row = []

        for column in range(gridSize):
            board_row.append(" ")

        battleBoard.append(board_row)
    return battleBoard
    
def display_board(board, gridSize):
    print()
    print("    A      B      C      D")

    for row in range(gridSize):
        print(" +-----+-----+-----+-----+")

        print(row +1, end=" ")

        for column in range(gridSize):
            print("|", end="")
            print(f"{board[row][column]:^5}", end="")

        print("|")
    
    print(" +-----+-----+-----+-----+")
    print()

    return

def convertLo (location):
    columnLetter = location[0]
    row = int(location[2]) - 1

    if columnLetter == "A":
        column = 0
    elif columnLetter == "B":
        column = 1
    elif columnLetter == "C":
        column = 2
    else:
        column = 3
    return row, column


def checkLo (location):
    while True:
        if len(location) == 3:
            if location[0] in "ABCD":
                if location[1] == ",":
                    if location[2] in "1234":
                        return location
                    break
                    
        print("Invalid location. Enter A, 1 through D, 4.")
        location = input(
            "Choose where you want to fire (Example A,1): "
        ).upper().replace(" "," ")
    

    
        

if __name__=="__main__":
    while True:
        try:
            
    
    print ("---- Battle Ship 1.0 ----")
    print ("")
    
    battleBoard= create_board()
    display_board(battleBoard)
    game = True

    locationList = []

    shiprow = 0
    shipcol = 0
    shiprow = random.randint(1,4)
    shipcol = random.randint(1,4)
    shiplocation = []
    shiplocation.append(shiprow-1)
    shiplocation.append(shipcol-1)

    # if battleBoard[shipcol-1][shiprow-1] == " ":
    #     battleBoard[shipcol-1][shiprow-1] = "ship"
    
    while game:
        location = (input("Choose where you want to fire (Example A,1): "))
        locationList.append(location)
        checkLo (location)
        row, col = convertLo(location)
        
        if [row,col] == shiplocation:
            print ("you win")
            game = False
        else: 
            battleBoard[row][col] = "x"
            display_board(battleBoard)
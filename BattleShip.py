import random


def create_board(gridSize):
    battleBoard = []


    for row in range(gridSize):
        board_row = []

        for column in range(gridSize):
            board_row.append(" ")

        battleBoard.append(board_row)
    return battleBoard
    
def display_board(battleBoard, gridSize):
    print()
    if gridSize == 4:
        print("    A      B     C     D")
    elif gridSize == 5:
        print("    A      B     C     D     E")
    elif gridSize == 6:
        print("    A      B     C     D     E      F")
    elif gridSize == 7:
        print("    A      B     C     D     E      F      G")
    elif gridSize == 8:
        print("    A      B     C     D     E      F      G      H")
    elif gridSize == 9:
        print("    A      B     C     D     E      F      G      H      I")
    elif gridSize == 10:
        print("    A      B     C     D     E      F      G      H      I      J")

    for row in range(gridSize):
        print(" +-----+-----+-----+-----+")

        print(row +1, end=" ")

        for column in range(4):
            print("|", end="")
            print(f"{battleBoard[row][column]:^5}", end="")

        print("|")
    
    print(" +-----+-----+-----+-----+")
    print()

    return

def convertLo (location, ):
    columnLetter = location[0]
    row = int(location[2]) - 1

    # fix to convert for boards bigger than 4
    if columnLetter == "A":
        column = 0
    elif columnLetter == "B":
        column = 1
    elif columnLetter == "C":
        column = 2
    elif columnLetter == "D":
        column = 3
    elif columnLetter == "E":
        column = 4
    elif columnLetter == "F":
        column = 5
    else:
        column = 3
    return row, column


def checkLo (location):
    while True:
        if len(location) == 3:
            if location[0] in "ABCDEFGHIJ":
                if location[1] == ",":
                    if location[2] in "123456789":
                        return location
                    break
        elif len(location) == 4:
            if location [0] in "ABCDEFGHIJ":
                if location[1] == ",":
                    if location[2] == "1":
                        if location[3] == "0":
                            return location
                        break                
        print("Invalid location. Enter A, 1 through D, 4.")
        location = input(
            "Choose where you want to fire (Example A,1): "
        ).upper().replace(" "," ")

def checkPlaceShip (placeShip, gridSize):
    while True:
        if len(placeShip) == 3:
            if placeShip[0] in "ABCDEFGHI":
                if placeShip[1] == ",":
                    if placeShip[2] in "123456789":
                        return placeShip
                    break
        elif len(placeShip) == 4:
            if placeShip [0] in "ABCDEFGHIJ":
                if placeShip[1] == ",":
                    if placeShip[2] == "1":
                        if placeShip[3] == "0":
                            return placeShip
                        break    

        print(f"Invalid location. Enter A,1 through D,{gridSize}.")
        placeShip = input(
            "Choose where you want to fire (Example A,1): "
        ).upper().replace(" "," ")

def convertPlaceShip (placeShip):
    columnLetter = placeShip[0]
    r = int(placeShip[2]) - 1

    if columnLetter == "A":
        c = 0
    elif columnLetter == "B":
        c = 1
    elif columnLetter == "C":
        c = 2
    else:
        c = 3
    return r, c    
        

if __name__=="__main__":
    print ("---- Battle Ship 1.1 ----")
    print ("")
    
    while True:
        try: 
            gridSize = int(input("Enter the size of your board. (Ex. 1-10): "))
            break
        except(ValueError):
            print ("Invalid input, try again.")
    print ("")

    battleBoard = create_board(gridSize)
    display_board(battleBoard,gridSize)
    game = True


    while True:
        try:
            shipChoice = (input("Do you want to place ship(s) randomly or manually?(r/m): "))
            if shipChoice.lower() == "r" or shipChoice.lower() == "m":
                break
            else:
                print ("Invalid input. Enter r/m")
        except:
            print ("Invalid input. Try again!")
    
    shipAmount = gridSize//2

    locationList = []
    ships = []
    if shipChoice.lower() == "r":
        for x in range (shipAmount):
            shiplocation = []
            shiprow = 0
            shipcol = 0
            shiprow = random.randint(1,gridSize)
            shipcol = random.randint(1,gridSize)
            shiplocation.append(shipcol-1)
            shiplocation.append(shiprow-1)
            ships.append(shiplocation)
    elif shipChoice.lower() == "m":
        
        for x in range (shipAmount):
            shiplocation = []
            while True:
                placeShip = input("Choose where you want to place ship (Ex. A,1)")
                checkPlaceShip(placeShip, gridSize)
                r, c = convertPlaceShip(placeShip)
                break
            if len(shiplocation) >= 1:

                for x in (shiplocation):
                    if r != x :
                        for d in (shiplocation):
                            if c != d:
                                shiplocation.append(placeShip)
                    else:
                        print ("Ship has already been placed here. Try again!")
                        shipAmount += 1
                        continue
            else:
                shiplocation.append(c)
                shiplocation.append(r)
            ships.append(shiplocation)
        
    # if battleBoard[shipcol-1][shiprow-1] == " ":
    #     battleBoard[shipcol-1][shiprow-1] = "ship"
    
    
    gamecount = 0
    while game:  #ismorethan
        if gamecount <= 5:
            location = (input("Choose where you want to fire (Example A,1): "))
            locationList.append(location)
            checkLo (location)
            row, col = convertLo(location)
            
            if len(ships) == 1:
                if [row,col] == ships:
                    print ("You hit. GOod job!")
                    print ("You won!")
                    game = False
                else: 
                    battleBoard[row][col] = "x"
                    display_board(battleBoard, gridSize)
                    gamecount += 1

            elif len(ships) > 1:
                for ship in (ships):
                    if [row,col] == ship:
                        print ("You hit a ship. GOod job!")
                        battleBoard[row][col] = "HIT!"
                        ships.remove(ship)
                        gamecount += 1
                    
                    else: 
                        battleBoard[row][col] = "x"
                
                display_board(battleBoard,gridSize)
                gamecount +=1
                
        else:
                    game = False 
                    print("Ran out of guesses, You Lose.")

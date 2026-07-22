import random

#creates board for game
def create_board(gridSize):
    battleBoard = []


    for row in range(gridSize):
        board_row = []

        for column in range(gridSize):
            board_row.append(" ")

        battleBoard.append(board_row)
    return battleBoard
    
#displays the board we created in a format
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

    printRow = ""
    for r in range (gridSize):
        printRow = printRow + "+-----"
    printRow = printRow + "+"
    print(printRow)
    for row in range(gridSize):
        
        if row > 0:
            print(printRow)
        print (row +1, end="")

        for column in range(gridSize):
            print("|", end="")
            print(f"{battleBoard[column][row]:^5}", end="")
        
        print("|")

    

    print(printRow)
    print()

    return


#converts input given for where they think the ship is, to usable values
def convertLo (location, ):
    columnLetter = location[0]
    row = int(location[2]) - 1
    abcS = ["A", 'B', "C", "D", "E", "F", "G", "H", "I", "J"]

    val = 0
    #loop sets col to the index based on the letter
    for letter in (abcS): 
        if columnLetter.upper() == letter:
            col = val
        else:
            val += 1

    return col, row


#validates input for location
def checkLo (location):
    while True:
        
        if int(location[2]) <= gridSize:
            if len(location) == 3:
                if location.upper()[0] in "ABCDEFGHIJ":
                    if location[1] == ",":
                        if location[2] in "123456789":
                            return location
                        break
            
            elif len(location) == 4:
                if location.upper() [0] in "ABCDEFGHIJ":
                    if location[1] == ",":
                        if location[2] == "1":
                            if location[3] == "0":
                                return location
                        break                
        
        else: 
            print("Invalid location. Enter A, 1 through D, 4.")
            location = input(
                "Choose where you want to fire (Example A,1): "
            ).upper().replace(" "," ")

#validates input for placing ship
def checkPlaceShip (placeShip, gridSize):
    while True:
        
        if len(placeShip[2]) <= gridSize:
            if len(placeShip) == 3:
                if placeShip.upper()[0] in "ABCDEFGHI":
                    if placeShip[1] == ",":
                        if placeShip[2] in "123456789":
                            return placeShip
                        break
            
            elif len(placeShip) == 4:
                if placeShip.upper()[0] in "ABCDEFGHIJ":
                    if placeShip[1] == ",":
                        if placeShip[2] == "1":
                            if placeShip[3] == "0":
                                return placeShip
                            break    

        else:
            print(f"Invalid location. Enter A,1 through D,{gridSize}.")
            placeShip = input(
                "Choose where you want to fire (Example A,1): "
            ).upper().replace(" "," ")


# converts input into usable information for checks
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
            if gridSize < 4 or gridSize > 10:
                print ("Invalid input. Try again.") 
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
            while True:
                try:
                    location = (input("Choose where you want to fire (Example A,1): "))
                    if len(location) < 3 or len(location) > 3:
                        print ("Invalid input. Try again.")
                    else:
                        break
                except:
                    print ("Invalid input. Try again.")
            locationList.append(location)
            checkLo (location)
            col, row = convertLo(location)
            
            if len(ships) == 1:
                if [col, row] == ships:
                    print ("You hit. GOod job!")
                    print ("You won!")
                    game = False
                else: 
                    battleBoard[col][row] = "x"
                    display_board(battleBoard, gridSize)
                    gamecount += 1

            elif len(ships) > 1:
                for ship in (ships):
                    if [col, row] == ship:
                        print ("You hit a ship. GOod job!")
                        battleBoard[col][row] = "HIT!"
                        ships.remove(ship)
                        gamecount += 1
                    
                    else: 
                        battleBoard[col][row] = "x"
                
                display_board(battleBoard,gridSize)
                gamecount +=1
                
        else:
                    game = False 
                    print("Ran out of guesses, You Lose.")

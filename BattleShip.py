import random

#creates board for game
def createPlayerBoard(gridSize):
    playerBoard = []
    enemyBoard = []

    for row in range(gridSize):
        board_row = []

        for column in range(gridSize):
            board_row.append(" ")

        enemyBoard.append(board_row)
    
    for row in range (gridSize):
        board_row = []

        for column in range (gridSize):
            board_row.append(" ")

        playerBoard.append(board_row)
    return playerBoard, enemyBoard
    

    
#displays player board we created in a format
def displayPlayerboard(playerBoard, enemyBoard, gridSize):
    print()
    for x in range (2):
        for s in range (2):
            print ("")
        board = None
        if x == 0:
            print ("Player's Board")
            board = playerBoard
        else: 
            print ("Enemy's Board")
            board = enemyBoard
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        needed = "   "
        index = 0
        for g in alphabet:
            if index >= gridSize:
                break
            else:
                needed = needed + g + "     "
                index += 1
        print(needed)        

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
                print(f"{board[column][row]:^5}", end="")
            
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
    print ("---- Battle Ship 1.2 ----")
    print ("")
    
    #determines the size of the grid(s)
    while True:
        try: 
            gridSize = int(input("Enter the size of your board. (Ex. 1-10): "))
            if gridSize < 4 or gridSize > 10:
                print ("Invalid input. Try again.") 
            break
        except(ValueError):
            print ("Invalid input, try again.")
    print ("")

    playerBoard, enemyBoard = createPlayerBoard(gridSize)

    displayPlayerboard(playerBoard,enemyBoard,gridSize)
    game = True


    #determines whether you want to place ships randomly or manually
    while True:
        try:
            shipChoice = (input("Do you want to place ship(s) randomly or manually?(r/m): "))
            if shipChoice.lower() == "r" or shipChoice.lower() == "m":
                break
            else:
                print ("Invalid input. Enter r/m")
        except:
            print ("Invalid input. Try again!")
    
    #calculates how many ships needed 
    shipAmount = gridSize//2


    
    playerships = []
    enemyships = []
    # randomly generates both player's and cpu's ship(s)
    for board in range (2):    
        if shipChoice.lower() == "r":
            for x in range (shipAmount):
                shiplocation = []
                shiprow = 0
                shipcol = 0
                shiprow = random.randint(1,gridSize)
                shipcol = random.randint(1,gridSize)
                shiplocation.append(shipcol-1)
                shiplocation.append(shiprow-1)
                if board == 0:
                    playerships.append(shiplocation)
                    playerBoard[shipcol-1][shiprow-1] = "SHIP"
                else:
                    enemyships.append(shiplocation)
        
        
        # loop to get ship placement
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
                if board == 0:
                    playerships.append(shiplocation)
                else:
                    enemyships.append(shiplocation)

    

    # if playerBoard[shipcol-1][shiprow-1] == " ":
    #     playerBoard[shipcol-1][shiprow-1] = "ship"
    
    playerGuess = [] # list for player guesses
    enemyGuess = [] #list for cpu guesses
    gamecount = 0
    while game:  
        
        if len(playerships) < 1 or len(enemyships) < 1:
            if len(playerships) < 1:
                print ("You hit all the ships. You win.")
                break
            elif len(enemyships) < 1:
                print ("You Lose. CPU hit all of the ships.")
                break
            elif gamecount <= 5:
                # player's guess
                for ship in range (shipAmount):    
                    enemyg = []
                    while True:
                        try:
                            location = (input("Choose where you want to fire (Example A,1): "))
                            if len(location) < 3 or len(location) > 3:
                                print ("Invalid input. Try again.")
                            else:
                                break
                        except:
                            print ("Invalid input. Try again.")
                    playerGuess.append(location)
                    checkLo (location)
                    col, row = convertLo(location)
                    
                    if len(enemyships) == 1:
                        if [col, row] == enemyships:
                            print ("You hit. GOod job!")
                            print ("You won!")
                            game = False
                        else: 
                            enemyBoard[col][row] = "x"
                            

                    elif len(playerships) > 1:
                        for ship in (enemyships):
                            if [col, row] == ship:
                                print ("You hit a ship. GOod job!")
                                enemyBoard[col][row] = "HIT!"
                                enemyships.remove(ship)
                            
                            else: 
                                enemyBoard[col][row] = "x"
                        
                    # cpu guess            
                    CPUrow = 0
                    CPUcol = 0
                    CPUrow = random.randint(1,gridSize)
                    CPUcol = random.randint(1,gridSize)
                    enemyg.append(CPUcol-1)
                    enemyg.append(CPUrow-1)

                    if len(playerships) == 1:
                        if [CPUcol, CPUrow] == playerships:
                            print ("You hit. GOod job!")
                            print ("You won!")
                            game = False
                        else: 
                            playerBoard[CPUcol-1][CPUrow-1] = "x"
                            

                    elif len(playerships) > 1:
                        for ship in (playerships):
                            if [CPUcol-1, CPUrow-1] == ship:
                                print ("You hit a ship. GOod job!")
                                playerBoard[col][row] = "HIT!"
                                playerships.remove(ship)
                                
                        
                            else: 
                                playerBoard[col][row] = "x"
                    displayPlayerboard(playerBoard, enemyBoard, gridSize)
                    gamecount+=1
            else:
                        game = False 
                        print("Ran out of guesses, You Lose.")

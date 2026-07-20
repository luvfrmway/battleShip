import random


def create_board():
    board = []

    for row in range(4):
        board_row = []

        for column in range(4):
            board_row.append(" ")

        board.append(board_row)

    return board

def display_board(board):
    print()
    print("    A      B      C      D")

    for row in range(4):
        print(" +-----+-----+-----+-----+")

        print(row +1, end=" ")

        for column in range(4):
            print("|", end="")
            print(f"{board[row][column]:^5}", end="")

        print("|")

    print(" +-----+-----+-----+-----+")
    print()

def randomLo():
    shipLocation = []
    for x in range(1):
        shiprow = 0
        shipcol = 0
        shiprow = random.randint(1,4)
        shipcol = random.randint(1,4)
        shipLocation.append(shiprow)
        shipLocation.append(shipcol)

        

def get_location():
    location = input("Enter location (Example A, 1): "
    ).upper().replace(" "," ")

    while True:
        if len(location) == 3:
            if location[0] in "ABCD":
                if location[1] == ",":
                    if location[2] in "1234":
                        return location
                    
        print("Invalid location. Enter A, 1 through D, 4.")
        location = input(
            "Enter location (Example A,1): "
        ).upper().replace(" "," ")

if __name__=="__main__":
    print ("---- Battle Ship 1.0 ----")
    print ("")
    display_board
    
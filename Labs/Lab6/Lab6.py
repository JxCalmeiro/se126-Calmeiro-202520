#Tony Calmeiro
#SE126.04
#Lab 6
#2-24-25

#PROGRAM PROMPT: This Program assigns seats in a small airplane with 7 rows (1-7) and 4 seats per row (A-D). It displays the seat layout, marking assigned seats with an 'X'. Users can reserve seats by typing their desired seat. If a seat is already taken, the program will notify the user and prompt them to choose another.

#--FUNCTIONS-------------------------------------------------------
def seatMap():
    print(f"\n{'ROW':3}   {'A':3} {'B':3}   {'C':3} {'D':3}")
    print("---------------------------------------------------------------")
    for i in range(len(seatsOccupied)):
        print(f"{i + 1:3}   {seatsOccupied[i][0]:3} {seatsOccupied[i][1]:3}   {seatsOccupied[i][2]:3} {seatsOccupied[i][3]:3}")
    print("---------------------------------------------------------------\n")

def continueReservation():
    response = input("Do you want to reserve another seat? (Y/N): ").upper()
    while response not in ["Y", "N"]:
        print("***INVALID ENTRY!***\nPlease try again\n")
        response = input("Do you want to reserve another seat? (Y/N): ").upper()
    return response

#--MAIN EXECUTING CODE---------------------------------------------

#--INITIALIZE 2D LIST-----------------------------------------------
seatsOccupied = [
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D']
]

# prints seat map
seatMap()

#--INITIALIZE VARIABLES---------------------------------------------
reserve_more = "Y"
seats_filled = 0

while reserve_more == "Y" and seats_filled < 28:
    # gets user input for row
    row_input = (input("Enter which row you'd like to sit in [1-7]: "))
    while not row_input.isdigit() or int(row_input) < 1 or int(row_input) > 7:
        print(f"\nYour input of '{row_input}' is Invalid! Please choose a row between 1 and 7.")
        row_input = (input("Enter which row you'd like to sit in [1-7]: "))
    
    row = int(row_input)

    # gets user input for seat
    seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ").upper()
    while seat not in ["A", "B", "C", "D"]:
        print(f"\nYour input of '{seat}' is Ivalid! Please choose a seat from A, B, C, or D.")
        seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ").upper()

    # finds seat index
    if seat == "A":
        seat_index = 0
    elif seat == "B":
        seat_index = 1
    elif seat == "C":
        seat_index = 2
    else:
        seat_index = 3

    # checks if seat is already occupied
    if seatsOccupied[row - 1][seat_index] == "X":
        print(f"\nSorry, seat {row}{seat} is already occupied. Please choose another one.")
    # assigns new seat and keeps count of occupied seats
    else:
        seatsOccupied[row - 1][seat_index] = "X"
        seats_filled += 1
        seatMap()

    # asks user if they would like to countinue reserving seats
    if seats_filled < 28:
        reserve_more = continueReservation()

# alerts user all seats are occupied and ends program
if seats_filled == 28:
    print("\nAll seats are occupied. No more reservations can be made.")

print("\nThank you for using our program to assign your seats.\nGoodbye!\n")
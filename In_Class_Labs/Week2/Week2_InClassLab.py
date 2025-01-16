#Tony Calmeiro
#SE126.04
#Week 2 - In CLass Lab
#1-16-2025

#PROGRAM PROMPT: This program displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY:
#total_records          The total amount of records that were processed from the csvfile
#rooms_over             The amount of rooms that are over capacity
#room                   The name of the room from (record[0]) of csvfile
#max_cap                The max capacity for the room from (record[1]) of csvfile
#people                 The number of meeting attending the meeting from (record[2]) of csvfile
#people_over            The amount of people over in the room (people - max_cap)

#--------MAIN EXECUTING CODE----------------------------------

import csv

#initializing needed variables
total_records = 0
rooms_over = 0

with open ("text_files/classLab2.csv") as csvfile:
    file = csv.reader(csvfile)
    
    #displays header
    print(f"\n{'ROOM':20}  {'MAX':4} {'PEOPLE':7} {'OVER'}")
    print("---------------------------------------------")

    #runs loop for each record in file
    for record in file:
        total_records += 1

        #pulls values for record and stores to variable
        room = record[0]    #name of room
        max_cap = int(record[1])     #max capacity of room
        people = int(record[2])     #number of people attending the meeting

        #determines if the room is over capacity
        if people > max_cap:
            rooms_over += 1
            people_over = people - max_cap

            print(f"{room:20} {max_cap:4} {people:4} {people_over:6}")

#prints summary
print("---------------------------------------------\n")
print(f"Processed {total_records} records")
print(f"There are {rooms_over} rooms over the limit\n")
print("Thank you for using the program, Goodbye!")

    

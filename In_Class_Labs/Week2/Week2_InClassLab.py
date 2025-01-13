#Tony Calmeiro
#SE126.04
#Week 2 - In CLass Lab
#1-16-2025

#PROGRAM PROMPT: This program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY:
#total_records
#csvfile
#record
#file
#room
#max
#min

#--------FUNCTIONS--------------------------------------------

#--------MAIN EXECUTING CODE----------------------------------

import csv

#initializing needed variables
total_records = 0

with open ("text_files/classLab2.csv") as csvfile:
    file = csv.reader(csvfile)
    
    print(f"{'ROOM':20}  {'MAX':4} {'MIN':4} {'OVER'}")
    print("------------------------------------")

    for record in file:
        total_records += 1

        room = record[0]    #name of room
        max = record[1]     #max capacity of room
        min = record[2]     #number of people attending the meeting

        print(f"{room:20} {max:4} {min:4}")

print("------------------------------------")
print(f"\nProcessed {total_records} records\n")


    

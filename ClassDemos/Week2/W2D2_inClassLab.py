#Tony Calmeiro
#SE126.04
#Week 2 - In CLass Lab
#1-16-2025

#PROGRAM PROMPT: This program displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY:
#total_rec              The total amount of records that were processed from the csvfile
#rooms_over             The amount of rooms that are over capacity
#name                   The name of the room from (record[0]) of csvfile
#max                    The max capacity for the room from (record[1]) of csvfile
#ppl                    The number of people attending the meeting from (record[2]) of csvfile
#remaining              The amount of people over in the room

#--------IMPORTS------------------------------------
import csv
#--------FUNCTIONS----------------------------------
def difference(people, max_cap):
    '''This function is passed 2 values and returns the difernece between them'''
    diff = max_cap - people
    return diff #this value will replace the difference() call in the main code

#--------MAIN EXECUTING CODE------------------------

#Initialize needed counting vars

total_rec = 0
rooms_over = 0

#displays header
print(f"{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER':5}")
print("----------------------------------------------")

#---------connected to the file------------------
with open("text_files/classLab2-1.csv") as csvfile:
    #must indent one level while connected to the file
    
    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (text file -> 2D list!)

        #assign each field data vaule to a friendly var name
        name = rec[0]    #name of room
        max = int(rec[1])     #max capacity of room         all text data is read as a string, so cast as a num!
        ppl = int(rec[2])     #number of people attending the meeting

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the rooms that are over capacity (remaining is negative)
        if remaining < 0 :
            rooms_over +=1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")

        #count ALL the rooms!
        total_rec += 1
#----------disconnected from thr file------------

#displat final data(counting vars)
print(f"\nRooms currently OVER capacity: {rooms_over}")
print(f"Total rooms in the file: {total_rec}")





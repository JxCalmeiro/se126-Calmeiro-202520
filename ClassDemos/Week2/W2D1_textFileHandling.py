#W2D1 - Text File Handling Intro Demo

#STEP 1: import the csv (comma seperated vaule) library
import csv

total_records = 0 #holds total num of records in file

#STEP 2: connect to the file
#--connected to file-----------------------------
#include relative file path in open()
#make sure \ switches to /
with open("text_files/simple.csv") as csvfile:
    #make sure to indent inside of code block

    #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2d list / matrix / table]
    file = csv.reader(csvfile)

    #print for headers
    print(f"{'NAME':10} {'NUM':3} {'COLOR'}")
    print("-----------------------------------")
    #STEP 3: process through every record (row) in the file
    for record in file:
        #add +1 to total_records to keep accurate count of records
        total_records += 1

        #print(record) #entire records/row data as list

        name = record[0]    #name field
        number = record[1]  #number field
        color = record[2]   #color field

        print(f"{name:10} {number:3} {color.title()}")
#--disconnected from file------------------------
print("-----------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")
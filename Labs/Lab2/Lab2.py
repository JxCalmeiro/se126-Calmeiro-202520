#Tony Calmeiro
#SE126.04
#Lab2
#1-20-2025
#
#PROGRAM PROMPT: This program reads a file containing computer specifications and displays a report that includes details for each computer listed. It will also display the total number of computers processed at the end of the program.

#VARIABLE DICTIONARY:
#computer_count
#computer_type
#brand
#cpu
#ram
#disk_one
#disk_two
#number_of_drives
#drive_num
#os
#year
#disk_two_or_os

#--------MAIN EXECUTING CODE----------------------------------

import csv

#initializing needed variables
computer_count = 0


with open ("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    
    #displays header
    print(f"\n{'Type':10} {'Brand':10} {'CPU':10} {'RAM(GB)':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':10} {'YR'}")
    print("-------------------------------------------------------------------------------------------------------------------")

    #runs loop for each record in file
    for record in file:
        computer_type = "Desktop" if record[0] == "D" else "Laptop"
        brand = record[1].replace("DL","Dell").replace("GW", "Gateway")
        cpu = record[2]
        ram = record[3]
        disk_one = record[4]
        number_of_drives = int(record[5])

        #assigns the correct record data to a variable for computers containing one disk drive
        if number_of_drives == 1:
            drive_num = record[5]
            os = record[6]
            year = record[7]
            disk_two_or_os = ""

        #assigns the correct record data to a variable for computers containing two disk drive
        else:
            drive_num = record[5]
            disk_two = record[6]
            os = record[7]
            year = record[8]
            disk_two_or_os = disk_two

        print(f"\n{computer_type:10} {brand:10} {cpu:10} {ram:10} {disk_one:10} {drive_num:10} {disk_two_or_os:10} {os:10} {year}")

        computer_count +=1

#displays the total number of computers processed
print(f"\nTotal number of computers: {computer_count}")


#Tony Calmeiro
#SE126.04
#Lab2
#1-20-2025

#PROGRAM PROMPT: This program reads a file containing computer specifications and displays a report that includes details for each computer listed. Then it will also display the total number of computers processed at the end of the program.

#VARIABLE DICTIONARY:
#computer_count             Total number of computers processed from the csvfile
#computer_type              Type of computer either 'Desktop' or 'Laptop'
#brand                      Manufacturer such as 'Dell', 'HP', or 'Gateway' 
#cpu                        Type of cpu being used in the computer
#ram                        Amount of Ram being used in the computer
#disk_one                   Amount of storage on disk 1 of the computer
#disk_two                   Amount of storage on disk 2 when there are 2 disks otherwise displays (------) when there is 1 disk
#number_of_drives           Reads if the computer has 1 or 2 drives,then uses an IF-Else statment to correctly assign the corresponding record to its variable to be displayed properly
#drive_num                  Displays the number of drives in the computer
#os                         The version of the operating system the computer is running
#year                       the year of the computer

#--------MAIN EXECUTING CODE----------------------------------

import csv

#initializing needed variables
computer_count = 0

#displays header
print(f"\n{'Type':10} {'Brand':10} {'CPU':10} {'RAM(GB)':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':5} {'YR'}")
print("--------------------------------------------------------------------------------------")

with open ("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

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
            disk_two = "------"         #used to display a blank space in column 7 for computers with one disk

        #assigns the correct record data to a variable for computers containing two disk drive
        else:
            drive_num = record[5]
            disk_two = record[6]        #used to display the disk size in column 7 for computers with two disks
            os = record[7]
            year = record[8]

        #displays the results pulled from the file in the loop
        print(f"\n{computer_type:10} {brand:10} {cpu:10} {ram:10} {disk_one:10} {drive_num:10} {disk_two:10} {os:5} {year}")

        #counts each computer processed in the file
        computer_count +=1

    #exit of loop

#displays the total number of computers processed
print("--------------------------------------------------------------------------------------")
print(f"\nTotal number of computers: {computer_count}")
print(f"\n~~~ End of Program ~~~")
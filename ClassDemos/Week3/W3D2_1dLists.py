#Tony Calmeiro
#SE126.04
#Week 2 - In CLass Lab
#1-27-25

#PROGRAM PROMPT: This program determines the cost of replacing all machines from 2016 or earlier, using a budget of $2,000 per desktop and $1,500 per laptop. Stores data from file to lists, displays the file's information, and generate a report summarizing the total number of machines, total number of desktops and laptops that need to be replaced, and replacement costs of desktops and laptops.

#VARIABLE DICTIONARY:
#computer_type              List for Type of computer either 'Desktop' or 'Laptop'
#brand                      List for Manufacturer such as 'Dell', 'HP', or 'Gateway' 
#cpu                        List for type of cpu being used in the computer
#ram                        List for amount of Ram being used in the computer
#disk_one                   List for amount of storage on disk 1 of the computer
#disk_two                   List for amount of storage on disk 2 when there are 2 disks otherwise displays (------) when there is 1 disk
#number_of_drives           List for the number of drives in the computer
#os                         List for the version of the operating system the computer is running
#year                       List for the year of the computer
#desktopCost                Total cost to replace old desktops (old_desktops * 2000)
#laptopCost                 Total cost to replace old laptops (old_laptops * 1500)
#totalCost                  Total cost to replace all old PCs (desktopCost + laptopCost)

#--IMPORTS-------------------------------------
import csv

#--MAIN EXECUTING CODE-------------------------

#created empty lists
computer_type = []                 #Computer Type -> D or L
brand = []                         #manufacture -> DL, FW, or HP
cpu = []                           #processor type
ram = []                           #total amount of RAM
disk_one = []                      #hard drive #1 size
number_of_drives = []              #number of disk drives -> 1 or 2
disk_two = []                      #hard drvie #2 size
os = []                            #machine operating system
year = []                          #machine year

#initializing needed variables

#--connected to file-------------------------------------------
with open ("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    #runs loop for each record in file
    for record in file:
        computer_type.append("Desktop" if record[0] == "D" else "Laptop")
        brand.append(record[1].replace("DL","Dell").replace("GW", "Gateway"))
        cpu.append(record[2])
        ram.append(record[3])
        disk_one.append(record[4])
        number_of_drives.append(int(record[5]))

        #assigns the correct record data to an index in the list(number_of_drives) for computers containing one disk drive
        if int(record[5]) == 1:
            disk_two.append("-----")          #used to display a blank space in column 7 for computers with one disk
            os.append(record[6])
            year.append(record[7])

        #assigns the correct record data to an index in the list(number_of_drives) for computers containing two disk drive
        else:
            disk_two.append(record[6])        #used to display the disk size in column 7 for computers with two disks
            os.append(record[7])
            year.append(record[8])

        #displays the results stored in the lists that are pulled from the file in the loop
    #for index in range(0, len(computer_type)):
        #print(f"\n{computer_type[index]:11} {brand[index]:10} {cpu[index]:5} {ram[index]:10} {disk_one[index]:10} {str(number_of_drives[index]):10} {disk_two[index]:10} {os[index]:5} {year[index]:5}")

        #counts each computer processed in the file

    #exit of loop
#--disconnected from file--------------------------------------

#process data from lists using a FOR loop *after* you are no longer connected to the file

#displays header
print(f"\n{'Type':11} {'Brand':10} {'CPU':5} {'RAM(GB)':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':5} {'YR':5}")
print("--------------------------------------------------------------------------------------")

#displays the results stored in the lists that are pulled from the file in the loop
for i in range(0, len(computer_type)):
        print(f"\n{computer_type[i]:11} {brand[i]:10} {cpu[i]:5} {ram[i]:10} {disk_one[i]:10} {str(number_of_drives[i]):10} {disk_two[i]:10} {os[i]:5} {year[i]:5}")

#counting for desktops and laptops that are old
old_desktops = 0            #from 2016 or earlier
old_laptops = 0             #from 2016 or earlier

for i in range(0, len(year)):
     if int(year[i]) <= 16:    #too old
        if computer_type[i] == "Desktop":
            old_desktops += 1

for i in range(0, len(year)):
     if int(year[i]) <= 16:    #too old
        if computer_type[i] == "Laptop":
            old_laptops += 1

#calculating costs to replace old desktops and laptops
desktopCost = old_desktops * 2000
laptopCost = old_laptops * 1500
totalCost = desktopCost + laptopCost

#displays final counts and cost results
print("--------------------------------------------------------------------------------------")
print(f"\nTotal number of computers: {len(computer_type)}")
print(f"\nDesktops that need to be replaced: {old_desktops}")
print(f"Cost to replace: ${desktopCost:.2f}")
print(f"\nLaptops that need to be replaced: {old_laptops}")
print(f"Cost to replace: ${laptopCost:.2f}")
print(f"\nTotal Cost to replace Desktops and Laptops: ${totalCost:.2f}")
print(f"\n~~~ End of Program ~~~")
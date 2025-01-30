# W4D2 - Sequential Seach Review + Creating & Writing to Text Files

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#--IMPORTS------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------

#--MAIN EXECUTING CODE------------------------------------

#--Initializing Lists-------------------------------------
dragons = []    #field0 - dragon names
riders = []     #field1 - rider names
counts = []     #field - 1 or 2, count of colors
color1 = []     #first primary color
color2 = []     #second color, only when count is 2

#--connected to file--------------------------------------
with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        counts.append(rec[2])
        color1.append(rec[3])

        if int(rec[2]) == 2:
            color2.append(rec[4])
        else:
            color2.append("-----")
#--disconnected to file-----------------------------------

print(f"\n{'DRAGONS':15}  {'RIDERS':30}  {'#':3}  {'COLOR1':8}  {'COLOR2':8}")
print("-----------------------------------------------------------------------")
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}  {riders[i]:30}  {counts[i]:3}  {color1[i]:8}  {color2[i]:8}")
print("-----------------------------------------------------------------------")

print(f"\nTotal number of Dragons: {len(dragons)}\n")

#SEARCH FOR A SPECIFIC DRAGON
#step 1: setup and gain of search
found = "x"
search = input("Which dragon are you looking for?: \n")

#step 2: perform search --> for loop w/ if statement
for i in range (0, len(dragons)):
    if search.lower() in dragons[i].lower():            #use in instead of == to be able search partial 
        #hold onto the found location (index) of our searched-for value
        found = i

#step 3: filter and display our results
if found != "x":
    print(f"\nYour search for {search} has ben FOUND: ")
    print(f"\n{dragons[found]:15}  {riders[found]:30}  {counts[found]:3}  {color1[found]:8}  {color2[found]:8}")
else:
    print(f"\nYour search for {search} was NOT FOUND :[")


#SEARCH FOR A COLOR SET
found = []
search = input("\nEnter the color you are looking for?: ")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found: #"if the foudn list is empty"
    print(f"\nYour search for {search} was NOT FOUND :[")
else:
    for i in range(0, len(found)):
         print(f"\n{dragons[found[i]]:15}  {riders[found[i]]:30}  {counts[found[i]]:3}  {color1[found[i]]:8}  {color2[found[i]]:8}")
    print(f"\nYour search for {search} was FOUND!")

#WRITE SOME DATA TO A FILE + CREATING SAID FILE
#create and write dragons and riders of the data to a new text file:

file = open("text_files/targs.csv", "w")

for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}")
file.close()
    
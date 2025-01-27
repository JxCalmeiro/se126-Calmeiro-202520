# W4D1 - Sequential Search

#PROGRAM PROMPT:Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1D lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new piece of data for each student: their current average test score.

#--IMPORTS---------------------------------------------------------
import csv
#--FUNCTIONS-------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >=80:
        let = "B"
    elif num >=70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num <= 60:
        let = "F"
    else:
        let = "ERROR"

    return let # the 'let' vaule will literally replace the letter() call in main code
   
#--MAIN EXECUTING CODE---------------------------------------------

#initialize a record counting variable
total_records = 0

#create some empty lists - one list for every potetial field in the file
fname = []
lname = []
test1 = []
test2 = []
test3 = []

#--connected to file-------------------------------------------------------------------
with open("text_files/class_grades-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

        # Store data from current record to corresponding lists (each field is its own!)
        # .append() --> adds the data to the next avaialble space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#--disconnected from file--------------------------------------------------------------

#process the lits to create and store each student's numeric average as well as letter grade average, then display all data back to the user
num_avg = []    #holds student's numeric avg: (test1 + test2 + test3) / 3
let_avg = []    #holds student's letter avg: letter(num_avg) return

for i in range(0, len(fname)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)

    let_avg.append(letter(a))

print(f"{'First':10}   {'Last':10}   {'T1':3}   {'T2':3}   {'T3':3}   {'# AVG':6}   {'L AVG'}")
print("----------------------------------------------------------")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}   {lname[i]:10}   {test1[i]:3}   {test2[i]:3}   {test3[i]:3}   {num_avg[i]:6.1f}   {let_avg[i]}")
print("----------------------------------------------------------")
print(f"Total Student in File: {len(fname)}")

#sequential search - search for a student by their LAST name

#step 1: set-up and gain search query
found = -1
search_last = input("Enter the last name you wish to find: ") #name we are looking for

#step 2: perform search algo (seq. search -> for loop w/ if statement)
for i in range(0, len(lname)):
    #for loop performs the SEQUENCE - from start through end of list items

    if search_last.lower() == lname[i].lower():
        #if performs the SEARCH - is what we're looking for here in the list?
        found = i   #stores found item's INDEX LOCATION

#step 3: display results to user; make sure you give infor: both for found or not found
if found != -1:
    #last name FOUND!
    print(f"Your search for {search_last} was FOUND! Here is their data: ")
    print(f"{fname[found]:10}   {lname[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {num_avg[found]:6.1f}   {let_avg[found]}")
else:
    #NOT FOUND
    print(f"Your search for {search_last} was NOT FOUND!")
    print("Check your cAsInG and sPeLlInG and try again!")

#Multples for letter grade
#step 1: set-up and gain search query
found = []
search_let = input("Enter the letter grade you wish to find: ") #name we are looking for

#step 2: perform search algo (seq. search -> for loop w/ if statement)
for i in range(0, len(let_avg)):
    #for loop performs the SEQUENCE - from start through end of list items

    if search_let.upper() == let_avg[i].upper():
        #if performs the SEARCH - is what we're looking for here in the list?
        found.append(i)   #stores found item's INDEX LOCATION
        print(f"Found a {search_let} grade in INDEX {i}")

#step 3: display results to user; make sure you give infor: both for found or not found
if not found: #'if not found' means 'found' is an empty list
    #NOT found
    print(f"Your search for {search_let} was NOT FOUND!")
    print("Check your cAsInG and sPeLlInG and try again!")
else:
    #letter grade FOUND!
    print(f"Your search for {search_let} was FOUND! Here is their data: ")
    for i in range(0, len(found)):
        print(f"{fname[found[i]]:10}   {lname[found[i]]:10}   {test1[found[i]]:3}   {test2[found[i]]:3}   {test3[found[i]]:3}   {num_avg[found[i]]:6.1f}   {let_avg[found[i]]}")

    

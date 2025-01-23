# W3D2 List review - 1Dimensional Lists & Parallel Lists

# PROMPT: Our W3D2 demo will focus on reviewing accessing text file data and storing the data into 1D lists. We will store the file data into respective lists, then process the data to print the information for each student as well as calculate and store a new piece of data for each student: their current average test score.

# this file uses: class_grades.csv

#--IMPORTS-------------------------------------------------------
import csv

#--FUNCTIONS-----------------------------------------------------

#--MAIN EXECUTING CODE-------------------------------------------

#initialize a record counting variable
total_records = 0

#--create empty list for potential field-------------------------
fname = []
lname = []
test1 = []
test2 = []
test3 = []

#--connecting to the file-------------
with open("text_files/class_grades.csv") as csvfile:
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
#--disconnected from the file---------

# processing lists -- USE A FOR LOOP
#for index in range(0, len(fname)):
    # for every item, index will satrt at 0 and ren up to (not including) the length ( # of items)
#    print(f"INDEX {index}: {fname[index]:10}  {lname[index]:10}  {test1[index]:3}  {test2[index]:3} {test3[index]:3}")

# create a newlist to hold each student's avg test score
avg = []

for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)

print(f"INDEX #:   {'FIRST':10}  {'LAST':11}  {'T1':3}  {'T2':3}  {'T3':3}  {'AVG'}")
print("-------------------------------------------------------------------------------------")
for index in range(0, len(fname)):
    # for every item, index will satrt at 0 and ren up to (not including) the length ( # of items)
    print(f"INDEX {index:3}: {fname[index]:10}  {lname[index]:10}  {test1[index]:3}  {test2[index]:3} {test3[index]:3}  {avg[index]:.2f}")
print("-------------------------------------------------------------------------------------")

#calc the entire class avg using a for loop to add each strdent's avg to the class total
total_avg = 0
for i in range(0, len(avg)):
    total_avg += avg[i]

class_avg = total_avg / len(avg)






print(f"\nTOTAL RECORDS: {total_records}\nCURRENT CLASS AVERAGE: {class_avg:.2f}")

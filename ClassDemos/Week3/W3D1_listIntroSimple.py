#W3D1 - List Introduction Simple
#This demo introduces lists working on the intro demo from Week 2

#This file uses: siple.csv

#--IMPORTS-------------------------------------------------------
import csv

#--MAIN EXECUTING CODE-------------------------------------------

#create empty lists
name = []
number = []
color = []

#--connected to file-----------------------------------------
with open("text_files/simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        
        name.append(record[0])               #name field
        number.append(int(record[1]))        #number field
        color.append(record[2])              #color field
#--disconnected from file------------------------------------

print(f"{'':8}{'NAME':10}    {'NUM'}    {'COLOR'}\n------------------------------------")

#process lists for printing
for index in range(0, len(name)):
    print(f"INDEX{index}: {name[index]:10}    {number[index]:3}    {color[index].title()}")

print("------------------------------------")
print(f"\nTotal Records:  {len(name)}\n")


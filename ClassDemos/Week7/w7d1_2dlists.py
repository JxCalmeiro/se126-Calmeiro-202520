#W7D1 - Introduction to 2D Lists

#2D lists are just lists of lists! 

#--IMPORTS------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------

#--MAIN EXECUTING CODE------------------------------------

two_d_list = [
    ['1','2','3','4'],
    ['5','6','7','8'],
    ['9','0','A','B'],
    ]

for i in range(len(two_d_list)):
    for x in range(len(two_d_list[i])):
        print(two_d_list[i][x], end='')
    print()
    
    
fileData = []

with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        fileData.append(rec)
        
#print(fileData)

#search_title = input("Enter the author to search for: ")

'''
for i in range(len(fileData)):
    for x in range(len(fileData[i])):
        #print(fileData[i][x])
        if search_title.lower() in fileData[i][x].lower():
            print(f"{fileData[i][0]:5}  {fileData[i][1]:35}  {fileData[i][2]:25}  {fileData[i][3]:17}  {fileData[i][4]:3}  {fileData[i][5]}")
'''

def seatMap():
    print(f"{'ROW':3}   {'A':3} {'B':3}   {'C':3} {'D':3}")
    print("---------------------------------------------------------------")
    for i in range(len(seatA)):
        print(f"{i + 1:3}   {seatA[i]:3} {seatB[i]:3}   {seatC[i]:3} {seatD[i]:3}")
    print("---------------------------------------------------------------")

seatA = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
seatB = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
seatD = ['D', 'D', 'D', 'D', 'D', 'D', 'D']

seatMap()

row = int(input("Enter which row you'd like to sit in [1-7]: "))
seat = input("Enter which seat you'd like to sit in [A/B/C/D]: ")
#W7D2 - Live Class: Review of Binary Search & Bubble Sort + 2D Lists

#This demo uses the file: simple.csv (also named simple-2.csv)

#this start file contains a "shell" program, or a coded outline, for the full working program we will build in class to review bubble sort and binary search, as well as introduce basic processing of 2D lists

import csv 


def menu():
    print("Simple Searching Menu")
    print("1. Search by NAME")
    print("2. Search by NUM")
    print("3. Search by COLOR")
    print("4. EXIT")

    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp


#create your empty 1D parallel lists
names = []
nums = []
colors = []

#we will use the below hand-populated list
valid_menu = ["1", "2", "3", "4"]

with open("text_files/simple.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title()) #just for Ray in the morning session
#disconnected from file-----------------------
ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu: 
        print("!INVALID ENTRY!\nPlease try again.\n")

    elif choice == "1": #search by NAME
        print("\n~Search by NAME~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search
        for i in range(len(names) - 1):
            for j in range(len(names) - 1):
                if names[j] > names[j + 1]:
                    #SWAP!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        #binary search
        search = input("Enter the name you are looking for?: ")

        min = 0                             #FIRST index
        max = len(names) - 1                #LAST index
        mid = int((min+max) / 2)            #MIDDLE index

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower():
                min = mid + 1

            mid = int((min+max) / 2)
        
        if search.lower() == names[mid].lower():
            print(f"We foudn your search for {search}, details below: ")
            print(f"{'NAME':12}  {'NUM':3}  {'COLOR':10}")
            print(f"-----------------------------")
            print(f"{names[mid]:12}  {nums[mid]:3}  {colors[mid]:10}")
            print(f"-----------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found :[\n")

    elif choice == "2": #search by NUM
        print("\n~Search by NUM~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    #SWAP!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        #binary search
        search = input("Enter the name you are looking for?: ")

        min = 0                             #FIRST index
        max = len(nums) - 1                #LAST index
        mid = int((min+max) / 2)            #MIDDLE index

        while min < max and search.lower() != nums[mid].lower():
            if search.lower() < nums[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower():
                min = mid + 1

            mid = int((min+max) / 2)
        
        if search.lower() == nums[mid].lower():
            print(f"We foudn your search for {search}, details below: ")
            print(f"{'NAME':12}  {'NUM':3}  {'COLOR':10}")
            print(f"-----------------------------")
            print(f"{names[mid]:12}  {nums[mid]:3}  {colors[mid]:10}")
            print(f"-----------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found :[\n")


    elif choice == "3": #search by COLOR
        print("\n~Search by COLOR~")

        #BUBBLE SORT -- *always* sort BEFORE we binary search
        for i in range(len(colors) - 1):
            for j in range(len(colors) - 1):
                if colors[j] > colors[j + 1]:
                    #SWAP!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        #binary search
        search = input("Enter the name you are looking for?: ")

        min = 0                             #FIRST index
        max = len(colors) - 1                #LAST index
        mid = int((min+max) / 2)            #MIDDLE index

        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower():
                min = mid + 1

            mid = int((min+max) / 2)
        
        if search.lower() == colors[mid].lower():
            print(f"We foudn your search for {search}, details below: ")
            print(f"{'NAME':12}  {'NUM':3}  {'COLOR':10}")
            print(f"-----------------------------")
            print(f"{names[mid]:12}  {nums[mid]:3}  {colors[mid]:10}")
            print(f"-----------------------------")
        else:
            print(f"\nYour search for {search} is complete, no matches found :[\n")

    else:
        print("\n~EXIT~")
        ans = "X" #ans changes from "y" to end the loop (condition will now eval as false)

print("\nThank you for using my program.\n\t\tGOODBYE!\n")


#------2D Lists ----------------------------------------------------------------------------------------------
#2D lists are just lists that contain 1D lists inside of them! 
print("\n\n\n2D Lists----------------------")
dataFile= []

with open("text_files/simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dataFile.append(rec)

for i in range(0, len(dataFile)):
    print(f"{dataFile[i]}")
    for j in range(0, len(dataFile[i])):
        print(f"{dataFile[i][j]} ", end="")
    print()




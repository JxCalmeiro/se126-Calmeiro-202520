#W7D1 - Binary Search & Bubble Sort Review

#PROGRAM SUMMARY: this program utilizes a menu that the user can choose from; it highlights instances of both sequential and binary search, along with the bubble sort algorithm when items must be sorted before display or binary search.

#this file uses: book_list.csv

#--IMPORTS------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------
def display(x,records):
    '''
        PARAMETERS:
        -x      signifier for if we are printing a single record or multiple
                when x != "x" it is an index and we have one value, otherwise we have multiple

        -records the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'LIB#':5}  {'TITLE':30}  {'AUTHOR':25}  {'GENRE':17}  {'PGS':3}  {'STATUS'}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{libNums[x]:5}  {titles[x]:35}  {authors[x]:25}  {genres[x]:17}  {pages[x]:3}  {status[x]}")

    elif found: #the found list is checked from the main code - when it is populated (has data) this statement evals as TRUE / when found is empty, it evals as FALSE
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{libNums[found[i]]:5}  {titles[found[i]]:35}  {authors[found[i]]:25}  {genres[found[i]]:17}  {pages[found[i]]:3}  {status[found[i]]}")
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{libNums[i]:5}  {titles[i]:35}  {authors[i]:25}  {genres[i]:17}  {pages[i]:3}  {status[i]}")

    print("----------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
    
def menu():
    '''This function shows a user the search menu and returns the user's choice'''
    print("\n\tPERSONAL LIBRARY MENU")
    print("\t1. Show All Titles") # – list all book data to the user alphabetically by title
    print("\t2. Show All Available")# – list all titles with status “available”
    print("\t3. Show All On Loan")# - show all titles with status “on loan”
    
    print("\t4. Search by Title") # – allow for an entire title or a title key word
    print("\t5. Search by Author")# – show all titles of the searched-for author
    print("\t6. Search by Genre")# - show all titles of the searched-for genre
    
    print("\t7. Search by Library Number")# – only allow for one specific library number item
    
    print("\t8. EXIT\n")
    
    choice = input("Enter your menu choice [1-8]: ")
    return choice
#--MAIN EXECUTING CODE------------------------------------

valid_menu = ["1", "2", "3", "4", "5", "6", "7", "8"]

libNums = []
titles = []
authors = []
genres =[]
pages = []
status = []

with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        libNums.append(int(rec[0]))
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(int(rec[4]))
        status.append(rec[5])
#disconnected from file---------------------

#main program -- housed inside of a loop for repeatability
ans = "y"
while ans == "y":
    found = [] #reset found back to empty for each new iteration
    menu_choice = menu() #return of menu() is stored to main program as 'menu_choice'
    
    #filter for what the user chose:
    if menu_choice not in valid_menu:
        #user did not follow the menu directions; alerts to them and then they will re-enter the loop
        print("***INVALID MENU CHOICE***")
        print("Please try again.\n")
    elif menu_choice == "1":
        print("\t1. Show All Titles") # – list all book data to the user alphabetically by title
        
        #sort the data by title 
        for i in range(0, len(titles) - 1):#outter loop
            for index in range(0, len(titles) - 1):#inner loop
                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(titles[index] > titles[index + 1]):
                    #swap data
                    swap(index, titles)
                    swap(index, libNums)
                    swap(index, authors)
                    swap(index, genres)
                    swap(index, pages)
                    swap(index, status)           

        # then display to the user -- "x" signifies to function that more than one location of data needs to be displayed!
        display("x", len(titles))
    
    elif menu_choice == "2":
        print("\t2. Show All Available")# – list all titles with status “available”
        
        #sequential search 
        search = "available"
        
        for i in range(0, len(status)):
            if search == status[i].lower():
                found.append(i)
        
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            display("x", len(found))
    
    elif menu_choice == "3":
        print("\t3. Show All On Loan")# - shlistow all titles with status “on loan”
    
    elif menu_choice == "4":
        print("\t4. Search by Title") # – allow for an entire title or a title key word
        
        search = input("\nEnter the TITLE or keyword of a title: ")
        
        for i in range(len(titles)):
            if search.lower() in titles[i].lower():
                found.append(i)
                
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            print(f"Your search for {search} is complete, please see details below: ")
            display("x", len(found))
    
    elif menu_choice == "5":
        print("\t5. Search by Author")# – show all titles of the searched-for author
    
    elif menu_choice == "6":
        print("\t6. Search by Genre")# - show all titles of the searched-for genre
    
    elif menu_choice == "7":
        print("\t7. Search by Library Number")# – only allow for one specific library number item
        
        search = int(input("Enter the LIBRARY NUMBER you are looking for: "))
        #SORT BY LIBRARY NUMBER
        for i in range(0, len(libNums) - 1):#outter loop
            for index in range(0, len(libNums) - 1):#inner loop
                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(libNums[index] > libNums[index + 1]):
                    #swap data
                    swap(index, titles)
                    swap(index, libNums)
                    swap(index, authors)
                    swap(index, genres)
                    swap(index, pages)
                    swap(index, status)
                    
        #binary search algorithm
        min = 0 
        max = len(libNums) - 1
        mid = int((min + max) / 2)
        
        while min < max and search != libNums[mid]:
            if search < libNums[mid]:
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search == libNums[mid]:
            print(f"Your search for {search} is complete, please see details below: ")
            display(mid, 0)
        else:
            print(f"Sorry, your search for {search} came up empty :[")
                
                    
    else:
        print("\t8. EXIT\n")
        ans = "x"
#end of main program loop-----------

print("\nThank you for using my program. Goodbye!\n")
    
            
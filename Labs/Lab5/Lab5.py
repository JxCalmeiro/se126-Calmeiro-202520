#Tony Calmeiro
#SE126.04
#Lab 5
#2-17-25

#PROGRAM PROMPT: This program stores the file data into 1D parallel lists, then uses the appropriate searching algorithms for the menu system options.  

#--IMPORTS---------------------------------------------------------
import csv

#VARIABLE DICTIONARY:
#lib_number = []                list holds values for library numbers
#title = []                     list holds values for book titles
#author = []                    list holds values for book authors
#genre = []                     list holds values for book genres
#page_count = []                list holds values for book page counts
#status = []                    list holds values for book status
#found = []                     list holds result values from search 
#ans                            allows user to enter search loop
#search_type                    allows user to input search option (1-8)
#search                         allows user to input search value
#min                            sets lowest possible index
#max                            sets highest index
#mid                            sets middle index in sorted list

#--FUNCTIONS-------------------------------------------------------
def display(x, records):
    print(f"\n{'LIB#':6} {'TITLE':35} {'AUTHOR':20} {'GENRE':17} {'PAGE CT':12} {'STATUS':9}")
    print("---------------------------------------------------------------------------------------------------------")

    if x != "x":
        #printing one record
        print(f"{lib_number[x]:6} {title[x]:35} {author[x]:20} {genre[x]:17} {page_count[x]:12} {status[x]:9}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{lib_number[found[i]]:6} {title[found[i]]:35} {author[found[i]]:20} {genre[found[i]]:17} {page_count[found[i]]:12} {status[found[i]]:9}")
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{lib_number[i]:6} {title[i]:35} {author[i]:20} {genre[i]:17} {page_count[i]:12} {status[i]:9}")
    
    print("---------------------------------------------------------------------------------------------------------")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#sequential search for exact match
def seqSearch1(search, listName):
    for i in range(0, len(listName)):
        if search.lower() == listName[i].lower():
            found.append(i)

#sequential search for key word match
def seqSearch2(search, listName):
    for i in range(0, len(listName)):
        if search.lower() in listName[i].lower():
            found.append(i)
            
#--MAIN EXECUTING CODE---------------------------------------------

#initialize a record counting variable

#--created lists-----------------------------------------------------
lib_number = []
title = []
author = []
genre = []
page_count = []
status = []

#--connected to file-----------------------------------------------
with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        lib_number.append(rec[0])           #library number field
        title.append(rec[1])                #title field
        author.append(rec[2])               #author field
        genre.append(rec[3])                #genre field
        page_count.append(rec[4])           #page count field
        status.append(rec[5])               #status: Available/On Loan field
#--disconnected to file--------------------------------------------

print("\n~~ Personal Library Catalog ~~")
ans = input("\nWould you like to enter the search program? [y/n]: ").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("\nWould you like to enter the search program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    found = [] #resets found list so each new menu/search it is empty

    #--displays data from search menu option--
    print("\nSearch Menu:")
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show All Available")
    print("7. Show All On Loan")
    print("8. Exit")

    search_type = input("\nEnter your search choice [1-8]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")

    # input #1 - Show All Titles
    elif search_type == "1":
        #BUBBLE SORT --> sorting for ascending alpha order
        for i in range(0, len(title) - 1):
            for j in range(0, len(title) - 1):
                if title[j] > title[j + 1]:
                    temp = title[j]
                    title[j] =  title[j + 1]
                    title[j + 1] = temp
                    #swap indices from parallel lists
                    swap(j, lib_number)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, page_count)
                    swap(j, status)
        print("\nAll Titles:")
        display("x", len(title))

    # input #2 - Search by Title
    elif search_type == "2":
        search = input("\nEnter the Title or Title key word to search: ")
        seqSearch2(search, title)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))

    # input #3 - Search by Author
    elif search_type == "3":
        search = input("\nEnter the Author to search: ")
        seqSearch1(search, author)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))

    # input #4 - Search by Genre 
    elif search_type == "4":
        search = input("\nEnter the Genre to search: ")
        seqSearch1(search, genre)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))

    # input #5 - Search by Library Number 
    elif search_type == "5":
        search = input("\nEnter the Library Number to search: ")
        #BUBBLE SORT --> sorting for ascending numerical order
        for i in range(0, len(lib_number) - 1):
            for j in range(0, len(lib_number) - 1):
                if lib_number[j] > lib_number[j + 1]:
                    temp = lib_number[j]
                    lib_number[j] =  lib_number[j + 1]
                    lib_number[j + 1] = temp
                    #swap indices from parallel lists
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, page_count)
                    swap(j, status)

        #BINARY SEARCH:
        min = 0                         #lowest possible index
        max = len(lib_number) - 1             #highest index
        mid = int((min + max) / 2)      #middle index in sorted list

        while min < max and search != lib_number[mid]:
            #while above is true, list is not yet exhausted and we haven't found what we are looking for, so must go through another searching iteration!
            if search < lib_number[mid]:
                max = mid - 1
            else: 
                #search > name[mid]
                min = mid + 1

            mid = int((min + max) / 2)

        if search.lower() == lib_number[mid].lower():
            print(f"\nWe have found your search for '{search}', see details below:")
            display(mid, len(lib_number))
        else:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")

    # input #6 - Show All Available 
    elif search_type == "6":
        seqSearch1("available", status)

        if not found:
            print(f"\nNo books are available at this time.")
        else:
            print(f"\nBooks that are available, see details below:")
            display("x", len(found))

    # input #7 - Show All On Loan 
    elif search_type == "7":
        seqSearch1("on loan", status)

        if not found:
            print(f"\nNo books are on loan at this time.")
        else:
            print(f"\nBooks that are on loan, see details below:")
            display("x", len(found))

    # input #8 - program exit
    elif search_type == "8":
        print(f"\n~~ Exiting the program. ~~")
        ans = "N"

#alert user that program is about to end
print(f"\nThank you for using the program.\nGoodbye!\n")
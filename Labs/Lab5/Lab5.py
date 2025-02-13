#Tony Calmeiro
#SE126.04
#Lab 5
#2-17-25

#PROGRAM PROMPT: This program stores the file data into 1D parallel lists, then uses the appropriate searching algorithms for the menu system options.  

#--IMPORTS---------------------------------------------------------
import csv

#VARIABLE DICTIONARY:

#--FUNCTIONS-------------------------------------------------------
#--search menu function--
def search_menu():
    choice = -1
    valid_answer = False

    # validates user input to write data
    while valid_answer == False:
        answer = (input("\nWould you like to use the search function? (Y/N): "))
        if answer.upper() == "Y" or answer.upper() == "N":
            valid_answer = True
        else:
            print(f"Your input of '{answer}' was Invalid, Please try again.")
    # prints search menu
    if answer.upper() == "Y":
        while choice != "8":
            print("\nSearch Menu:")
            print("1. Show All Titles")
            print("2. Search by Title")
            print("3. Search by Author")
            print("4. Search by Genre")
            print("5. Search by Library Number")
            print("6. Show All Available")
            print("7. Show All On Loan")
            print("8. Exit")

            choice = input("\nEnter your choice: ")

            # input #1 - Show All Titles
            if choice == "1":
                pass
            # input #2 - Search by Title
            elif choice == "2":
                pass
            # input #3 - Search by Author
            elif choice == "3":
                pass
            # input #4 - Search by Genre 
            elif choice == "4":
                pass
            # input #5 - Search by Library Number 
            elif choice == "5":
                pass
            # input #6 - Show All Available 
            elif choice == "6":
                pass
            # input #7 - Show All On Loan 
            elif choice == "7":
                pass
            # input #8 - program exit
            elif choice == "8":
                print(f"\n~~ Exiting the program. ~~")
            
            else:
                print(f"Your input of '{choice}' was Invalid, Please try again.")
    else:
        print(f"\n~~ Exiting the Program ~~")
    print(f"\nThank you for using the program.\nGoodbye!\n")

#--displays data from search menu option--
def multi_search(listFound):
    print("\nSearch Results:")
    print(f"\n{'LIB #':6} {'TITLE':35} {'AUTHOR':20} {'GENRE':17} {'PAGE CT':12} {'STATUS':9}")
    print("---------------------------------------------------------------------------------------------------------")
    for i in range(0, len(listFound)):
        print(f"{lib_number[listFound[i]]:6} {title[listFound[i]]:35} {author[listFound[i]]:20} {genre[listFound[i]]:17} {page_count[listFound[i]]:12} {status[listFound[i]]:9}")
    print("---------------------------------------------------------------------------------------------------------")
            
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

# print field headers
print(f"\n{'LIB #':6} {'TITLE':35} {'AUTHOR':20} {'GENRE':17} {'PAGE CT':12} {'STATUS':9}")
print("---------------------------------------------------------------------------------------------------------")

# processing through lists for display
for i in range(0, len(lib_number)):
    print(f"{lib_number[i]:6} {title[i]:35} {author[i]:20} {genre[i]:17} {page_count[i]:12} {status[i]:9}")
print("---------------------------------------------------------------------------------------------------------")

# calls search_menu function to allow user to search data
search_menu()
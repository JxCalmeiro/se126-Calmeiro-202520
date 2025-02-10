#Tony Calmeiro
#SE126.04
#Midterm Exam Choice 1
#2-10-25

#PROGRAM PROMPT: This program processes employee data from a file then stores data into parallel lists, the program will assign a unique office number to each employee and store that into a parallel list. Displays employee details in a formatted table, and generates a report summarizing total employees processed. The updated data is saved to a new file. The user also has an option to search for employees by (email or department).

#--IMPORTS---------------------------------------------------------
import csv
import random

#VARIABLE DICTIONARY:

#--FUNCTIONS-------------------------------------------------------
#--write data function--
def writeFile():
    # validates user input to write data
    valid_answer = False
    while valid_answer == False:
        answer = (input("\nWould you like to save data to file? (Y/N): "))
        if answer.upper() == "Y" or answer.upper() =="N":
            valid_answer = True
        else:
            print(f"Your input of '{answer}' was Invalid, Please try again.")
    # writes data to file (midterm_choice1.csv)
    if answer.upper() == "Y":
        file = open("text_files/midterm_choice1.csv", "w")
        for i in range(0, len(first_name)):
            line = (f"{first_name[i]},{last_name[i]},{email[i]},{department[i]},{phone_ext[i]},{office_num[i]}")
            if i < len(first_name) - 1:
                file.write(line + "\n")
            else:
                file.write(line)
                file.close()
        print("\n*** Data has sucessfully been written to file: 'midterm_choice1.csv' ***")
    else:
        print("\n*** Data was NOT written to file ***")

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
        while choice != "3":
            print("\nSearch Menu:")
            print("1. search by EMAIL")
            print("2. search by DEPARTMENT")
            print("3. Exit")

            choice = input("\nEnter your choice: ")

            # input #1 - email search
            if choice == "1":
                search = input("Enter the email to search for: ")
                found = False
                for i in range(0, len(email)):
                    if search.lower() == email[i].lower():
                        single_search(i)
                        found = True
                if not found:
                    print(f"No employee found with the email: {search}")

            # input #2 - department search
            elif choice == "2":
                search = input("Enter the department to search for: ")
                found = []
                for i in range(0, len(department)):
                    if search.lower() == department[i].lower():
                        found.append(i)
                if not found:
                    print(f"No employee found in department: {search}")
                else:
                    multi_search(found)

            # input #3 - program exit
            elif choice == "3":
                print(f"\n~~ Exiting the program. ~~")

            else:
                print(f"Your input of '{choice}' was Invalid, Please try again.")
    else:
        print(f"\n~~ Exiting the Program ~~")
    print(f"\nThank you for using the program.\nGoodbye!\n")       

#--displays data from single search menu option (1)--
def single_search(index):
    print("\nEmployee Found:")
    print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':6} {'OFFICE NUM':3}")
    print("---------------------------------------------------------------------------------------------")
    print(f"{first_name[index]:8} {last_name[index]:10} {email[index]:30} {department[index]:23} {phone_ext[index]:6} {office_num[index]:3}")
    print("---------------------------------------------------------------------------------------------")

#--displays data from multi search menu option (2)--
def multi_search(listFound):
    print("\nEmployees Found:")
    print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':6} {'OFFICE NUM':3}")
    print("---------------------------------------------------------------------------------------------")
    for i in range(0, len(listFound)):
        print(f"{first_name[listFound[i]]:8} {last_name[listFound[i]]:10} {email[listFound[i]]:30} {department[listFound[i]]:23} {phone_ext[listFound[i]]:6} {office_num[listFound[i]]:3}")
    print("---------------------------------------------------------------------------------------------")

#--MAIN EXECUTING CODE---------------------------------------------

#--created lists-----------------------------------------------------
first_name = []
last_name = []
email = []
department = []
phone_ext = []
office_num = []

#--connected to file-----------------------------------------------
with open("text_files/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first_name.append(rec[0])               #first name field
        last_name.append(rec[1])                #last name field
        email.append(rec[2])                    #email field
        department.append(rec[3])               #department field
        phone_ext.append(rec[4])                #phone extension field
#--disconnected to file--------------------------------------------

# generates office numbers for employees
for i in range(0, len(first_name)):
        office_num.append(random.randint(100, 200))

# print field headers
print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':6} {'OFFICE NUM':3}")
print("---------------------------------------------------------------------------------------------")

# processing through lists for display
for i in range(0, len(first_name)):
    print(f"{first_name[i]:8} {last_name[i]:10} {email[i]:30} {department[i]:23} {phone_ext[i]:6} {office_num[i]:3}")
print("---------------------------------------------------------------------------------------------")

#display total records processed
print(f"There was a total of {len(first_name)} employees processed.\n")

# calls writeFile function to write data to file (westeros.csv)
writeFile()

# calls search_menu function to allow user to search data
search_menu()
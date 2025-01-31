#Tony Calmeiro
#SE126.04
#Lab 4 w/ Search
#2-3-25

#PROGRAM PROMPT: This program processes employee data from a file to assign unique email addresses, departments, and phone extensions based on their House Allegiance. It stores data in parallel lists, displays employee details in a formatted table, and generates a report summarizing total employees and departmental counts. The updated data is saved to a new file.

#--IMPORTS---------------------------------------------------------
import csv
import random

#VARIABLE DICTIONARY:
#researchDevelopment_count = 0              counts the number of employees in the Research & Deveolpment Department.
#marketing_count = 0                        counts the number of employees in the Marketing Department.
#humanResources_count = 0                   counts the number of employees in the Human Resources Department.
#accounting_count = 0                       counts the number of employees in the Accounting Department.
#sales_count = 0                            counts the number of employees in the Sales Department.
#auditing_count = 0                         counts the number of employees in the Auditing Department.
#first_name = []                            list holds values for the First Name of employees.
#last_name = []                             list holds values for the Last Name of employees.
#age = []                                   list holds values for the Age of employees.
#screen_name = []                           list holds values for the Screen Names of employees.
#house_allegiance = []                      list holds values for the House Allegiance of employees.
#email_address = []                         list holds values for the Emails of employees.
#department = []                            list holds values for the Department employees are a part of.
#phone_extension = []                       list holds values for the Phone Extension of employees based on their Department.
#email                                      creates and email for the employee using their screen_name@westeros.net and stores it to the email_address list. "{screen_name[i]}@westeros.net"
#valid_answer = False                       variable is set to False, If user inputs "Y" or "N": sets variable to True and they will continue through loop, if invaild entry, program will prompt user to enter input again
#answer                                     if user input is "Y": program will process while loop in search function, user input is "N": program will exit

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
    # writes data to file (westeros.csv)
    if answer.upper() == "Y":
        file = open("text_files/westeros.csv", "w")
        for i in range(0, len(first_name)):
            line = (f"{first_name[i]},{last_name[i]},{email_address[i]},{department[i]},{phone_extension[i]}")
            if i < len(first_name) - 1:
                file.write(line + "\n")
            else:
                file.write(line)
                file.close()
        print("\n*** Data has sucessfully been written to file: 'westeros.csv' ***")
        # prints total number of employees written to the file
        print(f"\nThere was a total of {len(first_name)} employees saved to the file.")
        # prints total number of employees in each department
        print("\nDepartment Employee Totals:")
        print("---------------------------")
        print(f"Research & Development: {researchDevelopment_count}\nMarketing: {marketing_count}\nHuman Resouces: {humanResources_count}\nAccounting: {accounting_count}\nSales: {sales_count}\nAuditing: {auditing_count}")
    # does NOT write data to file    
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
        while choice != "5":
            print("\nSearch Menu:")
            print("1. search by FIRST NAME")
            print("2. search by PHONE EXT")
            print("3. search by LAST NAME")
            print("4. search by DEPARTMENT")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            # input # 1 - first name search
            if choice == "1":
                search = input("Enter the first name to search for: ")
                found = False
                for i in range(0, len(first_name)):
                    if search.lower() == first_name[i].lower():
                        single_search(i)
                        found = True
                if not found:
                    print(f"No employee found with the first name: {search}")

            # input # 2 - phone ext search
            elif choice == "2":
                search_input = input("Enter the phone ext to search for: ")
                if search_input.isdigit():      #ensures user inputs a numeric phone ext
                    search = int(search_input)
                    found = False
                    for i in range(0, len(phone_extension)):
                        if search == phone_extension[i]:
                            single_search(i)
                            found = True
                    if not found:
                        print(f"No employee found with the phone ext: {search}")
                else:
                    print(f"Your input of '{search_input}' was invalid, Please enter a numeric phone ext.")
            
            # input # 3 - last name search
            elif choice == "3":
                search = input("Enter the last name to search for: ")
                found = []
                for i in range(0, len(last_name)):
                    if search.lower() == last_name[i].lower():
                        found.append(i)
                if not found:
                    print(f"No employee found with the last name: {search}")
                else:
                    multi_search(found)

            # input # 4 - department search
            elif choice == "4":
                search = input("Enter the department to search for: ")
                found = []
                for i in range(0, len(department)):
                    if search.lower() == department[i].lower():
                        found.append(i)
                if not found:
                    print(f"No employee found in department: {search}")
                else:
                    multi_search(found)
            
            # input # 5 - program exit
            elif choice == "5":
                print(f"\n~~ Exiting the program. ~~")
            
            else:
                print(f"Your input of '{choice}' was Invalid, Please try again.")
    else:
        print(f"\n~~ Exiting the Program ~~")
    print(f"\nThank you for using the program.\nGoodbye!\n")

#--displays data from single search menu option (1 & 2)--
def single_search(index):
    print("\nEmployee Found:")
    print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
    print("-------------------------------------------------------------------------------")
    print(f"{first_name[index]:8} {last_name[index]:10} {email_address[index]:30} {department[index]:23} {phone_extension[index]:3}")
    print("-------------------------------------------------------------------------------")

#--displays data from multi search menu option (3 & 4)--
def multi_search(listFound):
    print("\nEmployees Found:")
    print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
    print("-------------------------------------------------------------------------------")
    for i in range(0, len(listFound)):
        print(f"{first_name[listFound[i]]:8} {last_name[listFound[i]]:10} {email_address[listFound[i]]:30} {department[listFound[i]]:23} {phone_extension[listFound[i]]:3}")
    print("-------------------------------------------------------------------------------")

#--MAIN EXECUTING CODE---------------------------------------------

#initialize a record counting variable
researchDevelopment_count = 0
marketing_count = 0
humanResources_count = 0
accounting_count = 0
sales_count = 0
auditing_count = 0

#--created lists-----------------------------------------------------
first_name = []
last_name = []
age = []
screen_name = []
house_allegiance = []
email_address = []
department = []
phone_extension = []

#--connected to file-----------------------------------------------
with open("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first_name.append(rec[0])               #first name field
        last_name.append(rec[1])                #last name field
        age.append(rec[2])                      #age field
        screen_name.append(rec[3])              #screen name field
        house_allegiance.append(rec[4])         #house allegiance field
#--disconnected to file--------------------------------------------

# generates email addresses
for i in range(0, len(first_name)):
    email = (f"{screen_name[i]}@westeros.net")
    email_address.append(email)

# assigns departments based on house allegiance
for i in range(0, len(first_name)):
    if house_allegiance[i] == "House Stark":
        department.append("Research & Deveolpment")
        researchDevelopment_count +=1
    elif house_allegiance[i] == "House Targaryen":
        department.append("Marketing")
        marketing_count += 1
    elif house_allegiance[i] == "House Tully":
        department.append("Human Resources")
        humanResources_count += 1
    elif house_allegiance[i] == "House Lannister":
        department.append("Accounting")
        accounting_count += 1
    elif house_allegiance[i] == "House Baratheon":
        department.append("Sales")
        sales_count +=1
    elif house_allegiance[i] == "The Night's Watch":
        department.append("Auditing")
        auditing_count +=1
    else:
        department.append("Unknown")

# generates random phone extensions based on department
for i in range(0, len(first_name)):
    if department[i] == "Research & Deveolpment":
        phone_extension.append(random.randint(100, 199))
    elif department[i] == "Marketing":
        phone_extension.append(random.randint(200, 299))
    elif department[i] == "Human Resources":
        phone_extension.append(random.randint(300, 399))
    elif department[i] == "Accounting":
        phone_extension.append(random.randint(400, 499))
    elif department[i] == "Sales":
        phone_extension.append(random.randint(500, 599))
    elif department[i] == "Auditing":
        phone_extension.append(random.randint(600, 699))
    else:
        phone_extension.append("Unknown")
    
# print field headers
print(f"\n{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("-------------------------------------------------------------------------------")

# processing through lists for display
for i in range(0, len(first_name)):
    print(f"{first_name[i]:8} {last_name[i]:10} {email_address[i]:30} {department[i]:23} {phone_extension[i]:3}")
print("-------------------------------------------------------------------------------")

# calls writeFile function to write data to file (westeros.csv)
writeFile()

# calls search_menu function to allow user to search data
search_menu()

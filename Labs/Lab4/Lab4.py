#Tony Calmeiro
#SE126.04
#Lab 4
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
#--function asking user if they would like to write data
def writeFile():
    #validates user input to write data
    valid_answer = False
    while valid_answer == False:
        answer = (input("\nWould you like to save data to file? (Y/N): "))
        if answer.upper() == "Y" or answer.upper() =="N":
            valid_answer = True
        else:
            print(f"Your input of '{answer}' was Invalid, Please try again.")
    # writes data to file (westeros_old.csv)
    if answer.upper() == "Y":
        file = open("text_files/westeros_old.csv", "w")
        for i in range(0, len(first_name)):
            line = (f"{first_name[i]},{last_name[i]},{email_address[i]},{department[i]},{phone_extension[i]}")
            if i < len(first_name) - 1:
                file.write(line + "\n")
            else:
                file.write(line)
                file.close()
        print("\n*** Data has sucessfully been written to file: 'westeros_old.csv' ***")
        # prints total number of employees written to the file
        print(f"\nThere was a total of {len(first_name)} employees saved to the file.")
        # prints total number of employees in each department
        print("\nDepartment Employee Totals:")
        print("---------------------------")
        print(f"Research & Development: {researchDevelopment_count}\nMarketing: {marketing_count}\nHuman Resouces: {humanResources_count}\nAccounting: {accounting_count}\nSales: {sales_count}\nAuditing: {auditing_count}")
    # does NOT write data to file    
    else:
        print("\n*** Data was NOT written to file ***")
    print(f"\n~~ Exiting the Program ~~")

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
        department.append("Research & Development")
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
    if department[i] == "Research & Development":
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

# calls function to write data to file (westeros.csv)
writeFile()

print(f"\nThank you for using the program.\nGoodbye!\n")
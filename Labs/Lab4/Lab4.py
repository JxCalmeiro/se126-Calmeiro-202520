#Tony Calmeiro
#SE126.04
#Week 3 - In CLass Lab
#2-3-25

#PROGRAM PROMPT:

#--IMPORTS---------------------------------------------------------
import csv
import random

#--FUNCTIONS-------------------------------------------------------

#--MAIN EXECUTING CODE---------------------------------------------

#initialize a record counting variable
answer = "Y"

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
        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(rec[2])
        screen_name.append(rec[3])
        house_allegiance.append(rec[4])
#--disconnected to file--------------------------------------------

# generate email addresses
for i in range(0, len(first_name)):
    email = (f"{screen_name[i]}@westeros.net")
    email_address.append(email)

# assign departments based on house allegiance
for i in range(0, len(first_name)):
    if house_allegiance[i] == "House Stark":
        department.append("Research & Deveolpment")
    elif house_allegiance[i] == "House Targaryen":
        department.append("Marketing")
    elif house_allegiance[i] == "House Tully":
        department.append("Human Resources")
    elif house_allegiance[i] == "House Lannister":
        department.append("Accounting")
    elif house_allegiance[i] == "House Baratheon":
        department.append("Sales")
    elif house_allegiance[i] == "The Night's Watch":
        department.append("Auditing")
    else:
        department.append("Unknown")

# generate phone extensions
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
print("-------------------------------------------------------------------------------\n")

# writes data to file (westeros.csv)
answer = (input("Would you like to save data to file? (Y/N): ")).upper()
if answer == "Y":
    with open("text_files/westeros.csv", "w", newline="") as westeros_file:
        for i in range(0, len(first_name)):
            writer = csv.writer(westeros_file)
            writer.writerow([first_name[i], last_name[i], email_address[i], department[i], phone_extension[i]])
    print("\n*** Data has sucessfully been written to file: 'westeros.csv' ***")
else:
    print("\n*** Data was NOT written to file ***")

print("\n~~ Thank you for using the program, Goodbye! ~~\n")


#Tony Calmeiro
#SE126.04
#Week 3 - In CLass Lab
#1-30-25

#PROGRAM PROMPT:

#VARIABLE DICTIONARY:

#--IMPORTS---------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >=80:
        let = "B"
    elif num >=70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num <= 60:
        let = "F"
    else:
        let = "ERROR"

    return let

#-----SEARCH MENU--------------------------------------------------
def search_menu():
    choice = 0
    while choice != "4":
        print("\nSearch Menu:")
        print("1. search by LAST NAME")
        print("2. search by FIRST NAME")
        print("3. search by LETTER GRADE")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the last name to search for: ")
            found = False
            for i in range(0, len(last_name)):
                if name.lower() == last_name[i].lower():
                    display_student(i)
                    found = True
            if not found:
                print(f"No student found with the last name: {name}")

        elif choice == "2":
            name = input("Enter the first name to search for: ")
            found = False
            for i in range(0, len(first_name)):
                if name.lower() == first_name[i].lower():
                    display_student(i)
                    found = True
            if not found:
                print(f"No student found with the first name: {name}")
            
        elif choice == "3":
            grade = input("Enter the letter grade to search for (A-F): ")
            found = []
            for i in range(0, len(let_avg)):
                if grade.upper() == let_avg[i].upper():
                    #display_student(i)
                    found.append(i)
            if not found:
                print(f"No students found with the letter grade: {grade}")
            else:
                display_grades(found)

        elif choice == "4":
            print("~~ Exiting the program. ~~\n")

        else:
            print("Invalid choice! Please try again.")

#-----DISPLAYS DATA FROM SEARCH MENU FUNCTION--------------------
def display_student(index):
    print("\nStudent Found:")
    print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'Average':8} {'Grade':6}")
    print("-------------------------------------------------------------")
    print(f"{first_name[index]:12} {last_name[index]:9} {test1[index]:6} {test2[index]:6} {test3[index]:6} {num_avg[index]:8.1f} {let_avg[index]:>4}")
    print("-------------------------------------------------------------")

def display_grades(listFound):
    print("\nStudent Found:")
    print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'Average':8} {'Grade':6}")
    print("-------------------------------------------------------------")
    for i in range(0, len(listFound)):
        print(f"{first_name[listFound[i]]:12} {last_name[listFound[i]]:9} {test1[listFound[i]]:6} {test2[listFound[i]]:6} {test3[listFound[i]]:6} {num_avg[listFound[i]]:8.1f} {let_avg[listFound[i]]:>4}")
    print("-------------------------------------------------------------")

#--MAIN EXECUTING CODE---------------------------------------------

#initialize a record counting variable
total_records = 0

#--empty lists-----------------------------------------------------
first_name = []
last_name = []
test1 = []
test2 = []
test3 = []

#--connected to file-----------------------------------------------
with open("text_files/class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        first_name.append(rec[0])
        last_name.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#--disconnected to file--------------------------------------------

num_avg = []
let_avg = []

# creates a number and letter average and adds to their respective lists.
for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)

    let_avg.append(letter(a))

# prints headers and displays data
print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'# Avg':8} {'Avg Grade':6}")
print("------------------------------------------------------------------")

for index in range(0, len(first_name)):
    print(f"{first_name[index]:12} {last_name[index]:9} {test1[index]:6} {test2[index]:6} {test3[index]:6} {num_avg[index]:8.1f} {let_avg[index]:>4}")
print("------------------------------------------------------------------")

# calculates class number average 
total_avg = 0
for i in range(0, len(num_avg)):
    total_avg += num_avg[i]

class_avg = total_avg / len(num_avg)

# displays total students and class number average
print(f"\nTotal Students: {total_records}\nCurrent Class Average: {class_avg:.1f}")

#--CALLS SEARCH MENU------------------------------------------------
search_menu()


#Tony Calmeiro
#SE126.04
#Week 4 - In CLass Lab
#1-30-25

#PROGRAM PROMPT: This program processes student test data from a file by storing it in lists, reprinting the original data, and calculating each student's average score, letter grade, and the class average. It also includes a search feature, allowing users to find students by last name, first name, or letter grade, displaying full details for matching records or alerting if no matches are found.

#VARIABLE DICTIONARY:
#total_records:             counts the number of records(students) that are processed
#first_name                 a list that holds data of the students first name
#last_name                  a list that holds data of the students last name
#test1                      a list that holds data of the students test1 numeric grade
#test2                      a list that holds data of the students test2 numeric grade
#test3                      a list that holds data of the students test3 numeric grade
#num_avg                    a list that holds data of the students average numeric grade, (test1[i] + test2[i] + test3[i]) / 3
#let_avg                    a list that holds data of the students average letter grade converted from their average numeric grade
#total_avg                  total average of all students processed, total_avg += num_avg[i]
#class_avg                  numeric grade average of the entire class of students processed, total_avg / len(num_avg)           
#choice = ""                users input of choice will process loop for choice entered(1, 2, 3, 4), if invaild entry, program will prompt user to enter input again
#valid_answer = False       variable is set to False, If user inputs "Y" or "N": sets variable to True and they will continue through loop, if invaild entry, program will prompt user to enter input again
#answer                     if user input is "Y": program will process while loop in search function, user input is "N": program will exit

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
    choice = ""
    valid_answer = False

    while valid_answer == False:
        answer = (input("\nWould you like to use the search function? (Y/N): "))
        if answer.upper() == "Y" or answer.upper() == "N":
            valid_answer = True
        else:
            print(f"Your input of '{answer}' was Invalid, Please try again.")
    if answer.upper() == "Y":
        while choice != "4":
            print("\nSearch Menu:")
            print("1. search by LAST NAME")
            print("2. search by FIRST NAME")
            print("3. search by LETTER GRADE")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            # last name search
            if choice == "1":
                name = input("Enter the last name to search for: ")
                found = False
                for i in range(0, len(last_name)):
                    if name.lower() == last_name[i].lower():
                        display_student(i)
                        found = True
                if not found:
                    print(f"No student found with the last name: {name}")

            # first name search
            elif choice == "2":
                name = input("Enter the first name to search for: ")
                found = False
                for i in range(0, len(first_name)):
                    if name.lower() == first_name[i].lower():
                        display_student(i)
                        found = True
                if not found:
                    print(f"No student found with the first name: {name}")

            # grade letter search    
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

            # program exit
            elif choice == "4":
                print(f"\n~~ Exiting the program. ~~")

            else:
                print(f"Your input of '{choice}' was Invalid, Please try again.")
    else:
        print(f"\n~~ Exiting the Program ~~")
    print(f"\nThank you for using the program.\nGoodbye!\n")

#-----DISPLAYS DATA FROM SEARCH MENU FUNCTION--------------------
def display_student(index):
    print("\nStudent Found:")
    print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'Average':8} {'Grade':6}")
    print("-------------------------------------------------------------")
    print(f"{first_name[index]:12} {last_name[index]:9} {test1[index]:6} {test2[index]:6} {test3[index]:6} {num_avg[index]:8.1f} {let_avg[index]:>4}")
    print("-------------------------------------------------------------")

def display_grades(listFound):
    print("\nStudents Found:")
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
print(f"\n{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'# Avg':8} {'Avg Grade':6}")
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
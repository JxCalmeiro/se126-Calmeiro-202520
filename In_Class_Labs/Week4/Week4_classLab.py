#Tony Calmeiro
#SE126.04
#Week 3 - In CLass Lab
#1-30-25

#PROGRAM PROMPT:

#VARIABLE DICTIONARY:

#--IMPORTS---------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------
#--SEARCH MENU-----------------------------------------------------
def search_menu():
    choice = None
    while choice != "4":
        print("\nSearch Menu")
        print("1. search by LAST name")
        print("2. search by FIRST name")
        print("3. search by LETTER GRADE")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the last name to search for: ").title()
            found = False
            for i in range(len(last_name)):
                if name == last_name[i]:
                    display_student(i)
                    found = True
            if not found:
                print("No student found with that last name")

        elif choice == "2":
            name = input("Enter the first name to search for: ").title()
            found = False
            for i in range(len(first_name)):
                if name == first_name[i]:
                    display_student(i)
                    found = True
            if not found:
                print("No student found with that first name")
            
        elif choice == "3":
            grade = input("Enter the letter grade to search for (A-F): ").upper()
            found = False
            for i in range(len(let_avg)):
                if grade == let_avg[i]:
                    display_student(i)
                    found = True
            if not found:
                print("No students found with that letter grade.")

        elif choice == "4":
            print("~~ Exiting the program. ~~\n")

        else:
            print("Invalid choice! Please try again.")

#--DISPLAYS DATA FROM SEARCH MENU FUNCTION-------------------------
def display_student(index):
    print("\nStudent Found:")
    print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'Average':8} {'Grade':6}")
    print("-------------------------------------------------------------")
    print(f"{first_name[index]:12} {last_name[index]:9} {test1[index]:6} {test2[index]:6} {test3[index]:6} {num_avg[index]:8.2f} {let_avg[index]:>4}")
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

for i in range(0, len(test1)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)

    if a >= 90:
        let_avg.append("A")
    elif a >= 80 and a <= 89.99:
        let_avg.append("B")
    elif a >= 70 and a <= 79.99:
        let_avg.append("C")
    elif a >= 60 and a <= 69.99:
        let_avg.append("D")
    else:
        let_avg.append("F")


print(f"{'Firstname':12} {'Lastname':12} {'Test1':6} {'Test2':6} {'Test3':6} {'Average':8} {'Grade':6}")
print("-------------------------------------------------------------")

for index in range(0, len(first_name)):
    print(f"{first_name[index]:12} {last_name[index]:9} {test1[index]:6} {test2[index]:6} {test3[index]:6} {num_avg[index]:8.2f} {let_avg[index]:>4}")
print("-------------------------------------------------------------")


total_avg = 0
for i in range(0, len(num_avg)):
    total_avg += num_avg[i]

class_avg = total_avg / len(num_avg)

print(f"\nTotal Students: {total_records}\nCurrent Class Average: {class_avg:.2f}")

#--CALLS SEARCH MENU------------------------------------------------
search_menu()


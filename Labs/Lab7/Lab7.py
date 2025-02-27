#Tony Calmeiro
#SE126.04
#Lab 6
#3-3-25

#PROGRAM PROMPT:

#--IMPORTS---------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------
def writeFile():
    file = open("text_files/updated_words.csv", "w")
    for key in pythonDict:
        file.write(f"{key},{pythonDict[key]}\n")
#--MAIN EXECUTING CODE---------------------------------------------

# empty dictionary
pythonDict = {}

# empty 2D list
dict2Dlist = []

# menu options list
menu_options = [
    "1. Show all words",
    "2. Search for a word",
    "3. Add a word",
    "3.5. Show words in alphabetical order",
    "4. EXIT"
]

#--connected to file-----------------------------------------------
with open("text_files/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        pythonDict.update({rec[0] : rec[1]})
        dict2Dlist.append(rec)
#--disconnected to file--------------------------------------------

for i in range(len(dict2Dlist)):
    for x in range(len(dict2Dlist[i])):
        print(dict2Dlist[i][x])

'''
print(f"{'Word':23} {"Definition"}")
print("-" * 185)
for key in pythonDict:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():20}\t{pythonDict[key]}")
print("-" * 185)
'''




# menu option loop
user_choice = -1

while user_choice != "4":
    print()
    print("-" * 30)
    print("My Programming Dictionary Menu")
    print("-" *30)
    
    for option in menu_options:
        print(option)

    user_choice = input("\nPlease choose an option: ")

    if user_choice == "1":
        print("\nAll words in the dictionary:")
        print("-" * 28)
        for key in pythonDict:
            print(key.upper())
        print("-" * 28)

    elif user_choice == "2":
        search = input("Enter the word you want to search for: ")
        found = 0
        for key in pythonDict:
            if search.lower() == key.lower():
                found = key
        if found != 0:
            print(f"We found your search for {search}, here is the info: \n")
            print(f"{'Word':23} {"Definition"}")
            print("-" * 185)
            print(f"{found.upper():20}\t{pythonDict[found]}")
            print("-" * 185)
        else:
            print(f"We could not find your search for '{search}' ")


    elif user_choice == "3":
        word = input("Enter the word you want to add: ")
        definition = input(f"Enter the definition for '{word}': ")
        if word in pythonDict:
            print(f"'{word}' already exists in the dictionary.")
        else:
            pythonDict.update({word: definition})
            print(f"'{word}' has been added to the dictionary.")

    elif user_choice == "3.5":
        print("\nWords in alphabetical order:")
        print("-" * 28)
        for word in sorted(pythonDict.keys()):
            print(word.upper())
        print("-" * 28)
            
    elif user_choice == "4":
            writeFile()
            print("\nChanges have been saved to 'updated_words.csv'\n~~ Exiting Program ~~")
    else:
        print("Invalid Choice. Please try again")

#alert user that program is about to end
print(f"\nThank you for using the program.\nGoodbye!\n")
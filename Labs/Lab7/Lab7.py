#Tony Calmeiro
#SE126.04
#Lab 7
#3-3-25

#PROGRAM PROMPT: This program lets users interact with a programming dictionary. Users can search for words, add new ones, view all words, exit via a menu, and saves updates to a new 'updated_words.csv' file

#--IMPORTS---------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------
#--write data function--
def writeFile():
    file = open("text_files/updated_words.csv", "w")
    for i in range(0, len(dict2Dlist)):
        line = (f"{dict2Dlist[i][0]},{dict2Dlist[i][1]}")
        if i < len(dict2Dlist) - 1:
            file.write(line + "\n")  # Add newline for all but last entry
        else:
            file.write(line)  # No newline after the last entry
    file.close()

# --Swap function for dict2Dlist when sorted--
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

# --Bubble Sort function for dict2Dlist--
def bubble_sort(dict2Dlist):
    for i in range(0, len(dict2Dlist) - 1):  # outer loop
        for index in range(0, len(dict2Dlist) - 1 - i):  # inner loop
            # Check if the current word (index 0 of the sublist) is greater than the next one
            if dict2Dlist[index][0] > dict2Dlist[index + 1][0]:
                # Swap if out of order
                swap(index, dict2Dlist)
#--MAIN EXECUTING CODE---------------------------------------------

# --empty dictionary--
pythonDict = {}

# --empty 2D list--
dict2Dlist = []

# --menu options list--
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

# --main menu loop--
user_choice = -1

while user_choice != "4":
    print()
    print("-" * 30)
    print("My Programming Dictionary Menu")
    print("-" *30)
    
    for option in menu_options:
        print(option)

    user_choice = input("\nPlease choose an option: ")

    # Shows all words
    if user_choice == "1":
        print("\nAll words in the dictionary:")
        print("-" * 28)
        for key in pythonDict:
            print(key.upper())
        print("-" * 28)

    # Search for a word
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


    # Add a word and definition
    elif user_choice == "3":
        word = input("Enter the word you want to add: ")
        definition = input(f"Enter the definition for '{word}': ")
        if word in pythonDict:
            print(f"'{word}' already exists in the dictionary.")
        else:
             # Add to the dictionary
            pythonDict.update({word: definition})
            # Add to the 2D list
            dict2Dlist.append([word, definition])
            print(f"'{word}' has been added to the dictionary.")

    # Sorts words alphabetically
    elif user_choice == "3.5":
        print("\nWords in alphabetical order:")
        bubble_sort(dict2Dlist)
        print("-" * 28)
        for entry in dict2Dlist:
            print(f"{entry[0].upper():20}")
        print("-" * 28)

    # saves to new file 'updated_words.csv' and exits program       
    elif user_choice == "4":
            writeFile()
            print("\nChanges have been saved to 'updated_words.csv'\n~~ Exiting Program ~~")
    
    # displays invalid entry for menu option choices
    else:
        print("Invalid Choice. Please try again")

#alert user that program is about to end
print(f"\nThank you for using the program.\nGoodbye!\n")
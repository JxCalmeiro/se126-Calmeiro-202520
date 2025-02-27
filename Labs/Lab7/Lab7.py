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

    for key in file:
        word = key[0].lower()
        definition = key[1]
        pythonDict[word] = definition

#--disconnected to file--------------------------------------------


print(f"{'Word':23} {"Definition"}")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for key in pythonDict:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():20}\t{pythonDict[key]}")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


# menu option loop
user_choice = -1

while user_choice != "4":
    print("\nMy Programming Dictionary Menu")
    print("------------------------------")
    
    for option in menu_options:
        print(option)

    user_choice = input("\nPlease choose an option: ")

    if user_choice == "1":
        print("All words in the dictionary:")
        for word in pythonDict:
            print(word)

    elif user_choice == "2":
        word = input("Enter the word you want to search for: ")
        if word in pythonDict:
            print(f"Definition of '{word}': {pythonDict[word]}")
        else:
            print(f"'{word}' is not in the dictionary.")

    elif user_choice == "3":
        word = input("Enter the word you want to add: ")
        definition = input(f"Enter the definition for '{word}': ")
        if word in pythonDict:
            print(f"'{word}' already exists in the dictionary.")
        else:
            pythonDict[word] = definition
            print(f"'{word}' has been added to the dictionary.")

    elif user_choice == "3.5":
        print("Words in alphabetical order:")
        for word in sorted(pythonDict.keys()):
            print(word)
            
    elif user_choice == "4":
            writeFile()
            print("Changes have been saved.\n~~ Exiting Program ~~")
    else:
        print("Invalid Choice. Please try again")

#alert user that program is about to end
print(f"\nThank you for using the program.\nGoodbye!\n")
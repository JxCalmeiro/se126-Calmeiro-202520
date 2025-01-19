#Tony Calmeiro
#SE126.04
#Lab3
#1-27-2025

#PROGRAM PROMPT: This program stores the potential voter data from the file into respective 1D lists. Processes the lists using a for loop to calculate and display the 4 labeled final totals and a total for records processed.

#VARIABLE DICTIONARY:
#idNumber                   List for ID Numbers of potential voters
#age                        List for age of potential voters
#registered                 List for if the potential voters are registered ("Y" or "N")
#voted                      List for those that did vote ("Y" or "N")
#notEligible                Total number that are too young and not eligible to register
#notRegistered              Total number of those old enough to vote but have not registered
#didNotVote                 Total number of those that are registered but did not vote
#didVote                    Total number of those that did vote

#--IMPORTS-------------------------------------
import csv

#--MAIN EXECUTING CODE-------------------------

#created empty lists
idNumber = []
age = []
registered = []
voted = []

#--connected to file-------------------------------------------
with open ("text_files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    #runs loop for each record in file
    for record in file:
        idNumber.append(record[0])
        age.append(int(record[1]))
        registered.append(record[2])
        voted.append(record[3])
    #exit of loop
#--disconnected from file----------------------------------------

#displays header
print(f"\n{'ID Number':12} {'Age':6} {'Registered':14} {'Voted':6}")
print("------------------------------------------")

#displays the results stored in the lists that are pulled from the file in the loop
for i in range(0, len(idNumber)):
    print(f"{idNumber[i]:12} {str(age[i]):10} {registered[i]:12} {voted[i]:6}")

#counting results for potential voters
notEligible = 0
notRegistered = 0
didNotVote = 0
didVote = 0

for i in range(0, len(age)):
    if (age[i]) < 18:                                               #too young to register
        notEligible += 1
    
    elif (age[i]) >= 18:
        if registered[i] == "N":                                    #old enough but not registered
            notRegistered += 1
        elif registered[i] == "Y" and voted[i] == "N":              #registered but did not vote
            didNotVote += 1
        elif registered[i] == "Y" and voted[i] == "Y":              #registered and voted
            didVote += 1

#displays final results
print("------------------------------------------")
print(f"\nNumber of individuals too young to register: {notEligible}")
print(f"\nNumber of individuals who are old enough to vote but have not registered.: {notRegistered}")
print(f"\nNumber of individuals who are eligible to vote but did not vote: {didNotVote}")
print(f"\nNumber of individuals who did vote: {didVote}")
print(f"\nTotal number of records processed: {len(idNumber)}")
print(f"\n~~~ End of Program ~~~\n")

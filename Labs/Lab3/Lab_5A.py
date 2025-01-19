#Jose Calmeiro
#Lab_5A.py
#11/17/2023
#Prog. Essentials Using Python, 202410_SE116.01A
#
#VARIABLE DICTIONARY:
#   notEligible         Accumulates total number of individuals not eligible to vote.
#   notRegistered       Accumulates total number of individuals not registered to vote.
#   didNotVote          Accumulates total number of individuals that did note vote.
#   voted               Accumulates total number of individuals that did vote.
#   totalRecords        Accumulates total number of records processed.
#   moreData            Allow user to input more data.
#   numID               User enters is ID Number.
#   age                 User enters in age.
#   register            User enters if registered to vote (Y/N).
#   vote                User enters if voted (Y/N).
#NOTES:
#   Ask user to input ID, Age, If registered, If Voted.
#   Prompt user to input more data.
#   Accumulate totals for each type of voter data:
#   -Not Eligible  -Not Registered  -Did Not Vote  -Voted  -Total Records
#   Display Accumulated totals back to user.  
#=====================================================================
notEligible = 0
notRegistered = 0
didNotVote = 0
voted = 0
totalRecords = 0
moreData = "Y"

while (moreData == "Y"):
    numID = str(input("Enter ID number: "))
    age = float(input("Enter Age : "))
    register = str (input("Are you registered to vote(Y/N)? ").upper())
    vote = str (input("Did you vote(Y/N)? ").upper())
    print("**********************************************")
    if age >= 18 and register == "Y" and vote == "Y":
        voted += 1
    if age >= 18 and register == "Y" and vote == "N":
        didNotVote += 1
    if age >= 18 and register == "N":
        notRegistered += 1
    if age < 18:
        notEligible += 1
        
    totalRecords += 1
    moreData = input("Would you like to enter in more data(Y/N)? ").upper()

print()
print()
print("**********************************************************************")
print("Voter Data Analysis:                                                 *")
print("Individuals not eligible to register: ",(notEligible),"                            *")
print("Individuals who are old enough to vote but have not registered: ",(notRegistered),"  *")
print("Individuals who are eligible to vote but did not vote: ",(didNotVote),"           *")
print("Individuals who did vote: ",(voted),"                                        *")
print("Number of records processed: ",(totalRecords),"                                     *")
print("**********************************************************************")
print()
print("Progam processing has completed.")
print('"Wisdom begins in wonder" - Socrates')

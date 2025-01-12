#Tony Calmeiro
#SE126.04
#Lab1
#1-13-2025
#
#PROGRAM PROMPT: This program checks if a meeting room complies with fire regulations for maximum capacity. It accepts the room's maximum capacity and the number of attendees, then determines whether the meeting is legal. If legal, it calculates how many more people can attend; if not, it specifies how many must be excluded. The program allows repeated checks for multiple rooms without exiting.
#
#VARIABLE DICTIONARY
#meeting_name       The name of the meeting, entered by user
#max_cap            The max capacity for the room, entered by user
#people             The number of meeting attending the meeting, entered by user
#diff               Difference of room capacity and people attending (max_cap - people)
#answer             loop control; value determines if loop repeats, entered by the user
#
#--------FUNCTIONS--------------------------------------------

def difference():
    '''This function determines the difference between the number of people attending the meeting against the rooms maximum capacity'''
    return max_cap - people

def decision():
    '''This function makes it so the user must provide a valid response'''
    ans = input("\t\tWould you like to check another meeting? [y/n]: ").lower()
    while ans != "y" and ans != "n":
        print("***INVALID ENTRY!***")
        ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()
    return ans

#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
answer = "y"

print("Welcome to the Fire Saftey Regulation Compliance Checker")
print()

#start of loop - will be based on answer
while answer == "y":

    meeting_name = input("Enter the name of the meeting [ex:Sales Meeting]:")
    max_cap = int(input("Enter the meeting rooms max capacity [ex:100]:"))
    people = int(input("Enter the number of people attending the meeting [ex:50]:"))

    diff = difference()

    #displays data to user
    if diff >= 0:
        print()
        print(f"The meeting '{meeting_name}' meets Fire Safety Regulations!")
        print(f"{diff} more people can be added to the meeting.")

    else:
        print()
        print(f"The meeting '{meeting_name}' is in violation of Fire Safety Regulations!")
        print(f"{abs(diff)} people must be removed from the meeting to meet Fire Safety Regulations.")

    #loop control
    answer = decision()

#out of loop

print("Thank you for using the program, Goodbye!")

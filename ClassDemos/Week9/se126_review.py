#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(index, listName):
    temp = listName[index]
    listName[index] =  listName[index + 1]
    listName[index + 1] = temp



#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list[len(names_list) - 1])       #last value


#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12,
    "age" : 12.5
}

print(people_dictionary) #displays ALL keys and values in the dict
print(people_dictionary["fname"]) 

#ceate an empty list fro each potential field
#these MUST remain the same length in order to be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#empty dictionary to store file data
dragons = {}

#gaining data from a text file 
with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
            temp_color = rec[4]
        else:
            color2.append("-----")
            temp_color = "-----"

        #adding data to a dictionary -- ({key : value})
        dragons.update({rec[0] : [rec[1], rec[2], rec[3], temp_color]})



#processing data from collections
#lists --> standard: for i in range()
print(f"{'NAMES':15} {'RIDERS':30} {'NUMS':6} {'COLOR1':8} {'COLOR2'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"{names[i]:15} {riders[i]:30} {nums[i]:6} {color1[i]:8} {color2[i]}")
print("-" * 75)

#dictionaries --> for key in collections
for key in dragons:
    print(f"{key.upper()} : {dragons[key]}") #this will show the valuse as a 1D list  to the console

    for value in dragons[key]:
        #loops through each value in the list found at the current key
        print(f"{key} - {value}", end="")
    print()

    for i in range(0, len(dragons[key])):
        print(f"{key} / {dragons[key][i]}")
    print("\n")

#searching & sorting
#SEQUENTIAL SEARCH -- searching in sequence through a collection
search = input("\nEnter the Dragons RIDER'S name you wish to find: ")

found = []

for key in dragons:
    if search.lower() in dragons[key][0].lower():
        found.append(key)

if not found: 
    print(f"\nwe couldnt find {search}.")
else:
    print(f"We found your search for {search}, here are the results: ")

    for i in range(len(found)):
        print(f"{found[i].upper():12} {dragons[found[i]][0]:30} {dragons[found[i]][1]:3} {dragons[found[i]][2]:8} {dragons[found[i]][3]}")


#searching & sorting
#BINARY SEARCH --> requires a set of ordered and unique data
#requires the soring of data before searching! BUBBLE SORT

for i in range(0, len(names) - 1):
    for j in range(0, len(names) - 1):
        if names[j] > names[j + 1]:
            #swap places!
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)
        
#binary --> bi means 2 --> we create a high and low half of the list
search = input("\nPlease enter the DRAGON NAME you wish to find: ")

min = 0
max = len(names) - 1
mid = int((min + max) / 2)

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record {mid}")
    print(f"{names[mid]:15} {riders[mid]:30} {nums[mid]:6} {color1[mid]:8} {color2[mid]}")
else:
    print(f"Sorry, we could not find your search for {search}.")


#2D lists - lists of lists! 
letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

print(letters)
print(letters[0])
print(letters[0][0])
print(letters[0][len(letters[0]) - 1])
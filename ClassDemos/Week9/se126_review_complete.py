#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j,listName):
    temp = listName[j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                               #entire list
print(names_list[0])                            #first value  [INDEX]
print(names_list[len(names_list) - 1])          #last value

#create an empty list for each potential field
# these MUST remain the same length in order to be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12, #no key name duplicates
    "age" : 12.5

}

print(people_dictionary)            #entire dictionary
print(people_dictionary["fname"])   #replaces with value assigned to "fname" key


dragon_dict = {}    #empty dictionary to be populated by the file

#gaining data from a text file 
with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0])        #.append() --> add to the end of a list
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
            color_var = rec[4]
        else:
            #still need to assign data for this dragon into color2 list so lists remain parallel
            color2.append("---")
            color_var = "---"

        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1], rec[2], rec[3], color_var]})



#processing data from collections
#lists --> standard for i in range():
print(f"{'NAMES':12} {'RIDERS':30} {'NUM':3} {'COLOR1':8} {'COLOR2'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 75)


#dictionaries --> for key in dictionary:
for key in dragon_dict:
    print(f"{key.upper():15} {dragon_dict[key]}") #this shows us the list data found at each key
    for value in dragon_dict[key]:
        print(f"{key} - {value}", end = "")
    print()
    for i in range(len(dragon_dict[key])):
        print(f"{key} / {dragon_dict[key][i]}", end = "")
    print("\n")
print("-" * 75)

#searching & sorting
#sequential search for multiple return values 
search = input("\nEnter the RIDER name you wish to find: ")
found = []

for key in dragon_dict:
    if search.lower() in dragon_dict[key][0].lower():
        print(key)
        found.append(key) #adds key of found location to the list 

if not found: 
    #found list is still empty, no search returned
    print(f"\nSorry, your search for {search} came up empty :[\n")
else:
    print(f"\nHere are the results for your search of {search}: ")
    for i in range(len(found)):
        print(f"{found[i].upper():15} {dragon_dict[found[i]][0]:30} {dragon_dict[found[i]][1]} {dragon_dict[found[i]][2]:8} {dragon_dict[found[i]][3]}")


#Binary Search *requires* the sorting of data before searching
#we must also ensure the collection we search through is populated with UNIQUE values

#bubble sort algorithm - a loop in a loop
for i in range(len(names) - 1):
    for j in range(len(names) - 1):
        if names[j] > names[j + 1]:
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)

search = input("\nEnter the DRAGON NAME you wish to find: ")

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
    print(f"\nWe found your search for {search} in record #{mid}, see info below:")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}\n")
else:
    print(f"\nSorry, we could not find your search for {search} :[\n")


#2D lists - lists of lists! 
letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

print(letters)              #whole 2d list (you will see multiple []s)
print(letters[0])           #first list inside of 2D letters
print(letters[0][0])        #first value in first list of 2D letters
print(letters[0][len(letters[0]) - 1]) #last value in first list of 2D letters

#letters[3][2]


goodboi= {
    "fname" : "George", 
    "mname" : "Bulleit", 
    "lname" : "Wayne",
    "age" : 12, 
    "roommates" : 3,
    "likesHugs" : False
}
for i in (key, value) in goodboi: 

       print(f"{key} {fname[0][1]} {mname[0][1]} {lname[0][1]} {age[0][1]} {roommates[0][1]} {likesHugs[0][1]}")

else:

       print("There is no data to display!")
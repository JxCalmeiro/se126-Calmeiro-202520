#Tony Calmeiro
#SE126.04
#Course Project - Top 200 Disney Grossng Films Search Program
#3-xx-25

#PROGRAM PROMPT:

#--IMPORTS---------------------------------------------------------
import csv

#--FUNCTIONS-------------------------------------------------------
def display(x, records):
    print(f"\n{'Rank':6} {'Year':6} {'Title':75} {'Production Studio':40} {'Genre':20} {'Worldwide Gross':15}")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    if x != "x":
        #printing one record
        print(f"{rank[x]:<6} {year[x]:<6} {title[x]:75} {prod_studio[x]:40} {genre[x]:20} ${int(gross[x]):15,}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{rank[found[i]]:<6} {year[found[i]]:<6} {title[found[i]]:75} {prod_studio[found[i]]:40} {genre[found[i]]:20} ${int(gross[found[i]]):15,}")
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{rank[i]:<6} {year[i]:<6} {title[i]:75} {prod_studio[i]:40} {genre[i]:20} ${int(gross[i]):15,}")
    
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#sorts data by Rank lowest to highest for search options
def rankSort():
    #BUBBLE SORT --> sorting for ascending numeric order
    for i in range(0, len(rank) - 1):
        for j in range(0, len(rank) - 1):
            if (rank[j]) > (rank[j + 1]):
                temp = rank[j]
                rank[j] =  rank[j + 1]
                rank[j + 1] = temp
                #swap indices from parallel lists
                swap(j, title)
                swap(j, year)
                swap(j, prod_studio)
                swap(j, genre)
                swap(j, gross)

#swaps indicies when bubble sorting
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#sequential search for exact match
def seqSearch1(search, listName):
    for i in range(0, len(listName)):
        if search.lower() == listName[i].lower():
            found.append(i)

#sequential search for key word match
def seqSearch2(search, listName):
    for i in range(0, len(listName)):
        if search.lower() in listName[i].lower():
            found.append(i)

#prints choice list for search option 6
def studioList():
    for i in range(0, len(studioChoices)):
        print(f"{studioChoices[i]}")

#prints choice list for search option 7
def genreList():
    for i in range(0, len(genreChoices)):
        print(f"{genreChoices[i]}")


#--created lists-----------------------------------------------------
#Static Lists
studioChoices = ["Disney-Pixar", "Disneytoon Studios", "Lucasfilm", "Marvel Studios", "Walt Disney Animation Studios", "Walt Disney Pictures"]
genreChoices = ["Action", "Adventure", "Comedy", "Drama", "Musical", "Romantic Comedy", "Western"]
# Appended Lists
rank = []
year = []
title = []
prod_studio = []
genre = []
gross = []

#--MAIN EXECUTING CODE---------------------------------------------

#--connected to file-----------------------------------------------
with open("text_files/disney_movies.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        rank.append(int(rec[0]))
        year.append(int(rec[1]))
        title.append(rec[2])
        prod_studio.append(rec[3])
        genre.append(rec[4])
        gross.append(int(rec[5]))
#--disconnected from file-------------------------------------------

# main searching loop
prog_title = "~~ Welcome to the Top 200 Grossing Disney Films Search Program! ~~"
width = 115
print()
print(prog_title.center(width))
print("------------------------------------------------------------------------------------------------------------------------")
print("This program provides easy access to detailed information on Disney's highest-grossing films. Whether you're interested \nin exploring the full list of films, searching by specific criteria, or finding particular films by its rank, genre, \nor year, this tool offers various options to help you quickly find the information you're looking for.")
print("------------------------------------------------------------------------------------------------------------------------")

ans = input("\nWould you like to enter the search program? [y/n]: ").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("\nWould you like to enter the search program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    found = [] #resets found list so each new menu/search it is empty

    #--displays data from search menu option--
    print("\nSearch Menu:")
    print("1. Show All Films Alphabetically")
    print("2. Search by Film Title")
    print("3. Show All Films by Rank")
    print("4. Search by Film Rank")
    print("5. Search All Films by Year")
    print("6. Search by Production Studio")
    print("7. Search by Film Genre")
    print("8. Exit")

    search_type = input("\nEnter your search choice [1-8]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")

    # input #1 - Show All Films Alphabetically
    elif search_type == "1":
        #BUBBLE SORT --> sorting for ascending alpha order
        for i in range(0, len(title) - 1):
            for j in range(0, len(title) - 1):
                if title[j] > title[j + 1]:
                    temp = title[j]
                    title[j] =  title[j + 1]
                    title[j + 1] = temp
                    #swap indices from parallel lists
                    swap(j, rank)
                    swap(j, year)
                    swap(j, prod_studio)
                    swap(j, genre)
                    swap(j, gross)
        print("\nAll Films Alphabetically:")
        display("x", len(title))
    
    # input #2 - Search by Film Title
    elif search_type == "2":
        search = input("\nEnter the Title or Title key word for the Film to search: ")
        seqSearch2(search, title)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))

    # input #3 - Show All Films by Rank
    elif search_type == "3":
        rankSort()
        print("\nAll Films by Rank:")
        display("x", len(rank))

    # input #4 - Search by Film Rank
    elif search_type == "4":
        search = int(input("\nEnter the Film Rank to search: "))
        rankSort()
        
        #BINARY SEARCH:
        min = 0                         #lowest possible index
        max = len(rank) - 1             #highest index
        mid = int((min + max) / 2)      #middle index in sorted list

        while min < max and search != rank[mid]:
            if search < rank[mid]:
                max = mid - 1
            else: 
                #search > name[mid]
                min = mid + 1

            mid = int((min + max) / 2)

        if search == rank[mid]:
            print(f"\nWe have found your search for '{search}', see details below:")
            display(mid, len(rank))
        else:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        
    # input #5 - Search All Films by Year
    elif search_type == "5":
        search = int(input("\nEnter the Year to search: "))
        rankSort()
        for i in range(0, len(year)):
            if search == year[i]:
                found.append(i)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))
    
    # input #6 - Search by Production Studio
    elif search_type == "6":
        print(f"\nChoices:")
        studioList()
        search = input("\nEnter the Film Production Studio to search: ")
        rankSort()
        seqSearch1(search, prod_studio)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))


    # input #7 - Search by Film Genre
    elif search_type == "7":
        print(f"\nChoices:")
        genreList()
        search = input("\nEnter the Film Genre to search: ")
        rankSort()
        seqSearch1(search, genre)

        if not found:
            print(f"\nSorry, we could not find your search for '{search}'. Please try again.")
        else:
            print(f"\nWe have found your search for '{search}', see details below:")
            display("x", len(found))

    
    # input #8 - Program Exit
    elif search_type == "8":
        print(f"\n~~ Exiting the program. ~~")
        ans = "N"

#alert user that program is about to end
print(f"\nThank you for using the program.\nGoodbye!\n")
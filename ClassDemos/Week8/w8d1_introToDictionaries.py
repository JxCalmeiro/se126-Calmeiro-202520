#W8D1 - Intro to Dictionaries

#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 

#--IMPORTS--

#--MAIN EXECUTING CODE--

#start by creating a populated dictionary
myCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "Focus SE Hatchback",
    "year" : 2014,
    "name" : "Gwendoline",
    "color" : "black"
    #key names CANNOT be repeated / NO DUPLICATES of keys!
}

#view the entire  dictionary and all of its data
print(myCar)

#view a specific value from the dictionary --> name[key] --> value
print(f"My car is a {myCar["make"]} {myCar["model"]}. It is {myCar["color"]}")

yourCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "F-150",
    "year" : 2024,
    "name" : "Gandalf",
    "color" : "black",
    "friends" : ["Tyler", "Tony", "Steve"]
}

print(f"My car is a {yourCar["make"]} {yourCar["model"]}. It is {yourCar["color"]}")

#add some data to a dictionary once ceated
yourCar["plate"] = "12345"

#or use the .update({key:value}) method
yourCar.update({"wheels" : "4"})

for key in yourCar:
    #for every key stored to the yourCar dictionary
    print(f"{key.upper():10}\t{yourCar[key]}")
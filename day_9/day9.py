programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again"
}

print(programming_dictionary["Function"])

#Create an empty dictionary
empty_dictionary={}

#Wipe an existing dictionary
#programming_dictionary={}
#print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"]="Edited Bug"
print(programming_dictionary)

#Loop through a dictionary - gives the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
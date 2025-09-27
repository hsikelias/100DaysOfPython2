# import random
# import headsTails    #its empty but now its a module we created.


# ran = random.randint(1,10) # generates a random integer between a and b, a and b are the numbers we provide A <= N <= B, the output gives out a random number between
# # the a and b we provide
# print(ran)

# # MODULE: 

# # some important stuff can be converted to module, like in this case random is an important feature so we have a seperate module for it.
# # in future, if theres a function that repeats a lot.. we can turn it into a module

# # this allows collabaration too, different people working on different module.
# # __init__.py have this file inside a directory containing modules if theres many modules.


# random_numfloat = random.random() #generates a floating number between 0.0 and 1.0
# print(random_numfloat)

# random_num = random.random()*10.  # if you dont need float
# print(random_num)

# random_numuni = random.uniform(10,20) #generates a floating number between the numbers you input
# print(random_numuni)



## LISTS

# a way of organizing and storing data in python, especially grouped data because even variables can store one data
# these grouped data usually maintain a relationship

# fruits = [item1, item2]
# you can store anything: num, string, bools.. [] is the syntax to recognize a list.

list = [0,True,"string", 5.6345]
#.              0.         1.         2.         3.           #4
state_names=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# you can ofcourse access the data in this list
# to access the first data in a list you need to use 0
print(state_names[0])

# think of these data as shifting values instead of their current position.. liek Alabama is at the first so no shift, alaska then gets shifted
# by 1 and arizona by 2
print(state_names[0:3]) # to access more than one data

# NEGATIVE INDEX

# having negative index is possible, like -1 counts from the end of the list

print(state_names[-1])

# how to alter the data inside a list

state_names[0]= "Sweet home alabama"
print(state_names[0])

state_names.append("New land") #adds a new data to the list, use the .extend to add one more data to the list
print(state_names[-1])

# Index error
# this happens when you try to access certain data from a list that doesnt exist.. basically youre way beyond the last value. 

print(len(state_names))


# Nested lists

name = ["tom", "bom", "slom", "plam","glam"]
last_name = ["brim","brom","tram","fram","trye"]
print(name,last_name)
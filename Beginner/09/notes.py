# DICTIONARY

'''
Dictionaries in python work pretty much like what it does in real world,you have a word and u use dictionary to find its meaning.So the word is the KEY and its definition is the VALUE

SYNTAX: 
{"key": value}

'''
# this is how u can add multiple keys and values also making sure it's readable
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again,"
  }

# how to retrieve an item from dictionary?
# unlike lists where we use [0],[1]. For dictionaries we use its key that could be som like programming_dictionary["Bug"]

print(programming_dictionary["Bug"])

# Adding new items to the dictionary

programming_dictionary["Test"] = "This is not a test"

# How to assign a value to an existing key in dictionary

programming_dictionary["Bug"] = "Not bug"
print(programming_dictionary)

# Empty dictionary 
emptyDic = {}

# LOOPIN THRU DICTIONARIES

for key in programming_dictionary:
  print(key)  # Output: Bug, Function, Loop, Test


capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# ^ ^ Hard to manage, better way to do this is to nest dictionaries/lists inside the existing dictionary
'''
travel_log = {
  "France": ["Paris","Lille","Dijon"],
  "Germany": ["Stuttgart","Berlin"],
}'''

# LIST IN LIST 

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

travel_log = {
  "France": 
  {
    "cities_visited": ["Paris","Lille","Dijon"],
    "total_visits": 8
  },
  "Germany": 
  { 
    "cities_visited":[ "Stuttgart","Berlin","Hamburg"],
    "total_visits": 5
  },
}

print(travel_log["Germany"]["cities_visited"][0])

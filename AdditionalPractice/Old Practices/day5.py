# Today learning goals

# Python dictionary, nesting

# every dictionary has a key(the word) and its associated value(definition)
# dictionary in python is recognized with {}

dic1 = {"key":"value"}
dic2 = {
    "bug":"pain",
    "debug":"extra pain"
    }

# how to access an item from dictionary
# similar to list but dictionaries uses the key to identify 

print(dic2["bug"])

dic2["debug"] = "true"
print([dic2])

empty_dictionary = {}
# or just do below thing
# dic2 = {}
# print([dic2])
# wipe an existing dictionary

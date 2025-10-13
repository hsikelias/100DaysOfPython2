## LOOPS


# for loop
# for item in list_of_items:
#     do something to each item

fruits = ["Apple", "Peach", "Pear"]
# to access each item in the list
for fruit in fruits: 
# here the single item we are tryna access is fruit, its assigning each item in the list to fruit one by one
  print(fruit)

# output: Apple, Peach, Pear
# for loops arent just used for printing things in a list, we can repeat a whole bunch of code.

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: 
  print(fruit)
  print(fruit + " Pie")

# loops are really handy when you need to repeat a task


# RANGE

# a really useful function if you wanna generate a range of numbers to loop thru

for number in range(4,9):
  print(number)   # output = 4,5,6,7,8

# theres soemthing interesting about the range function which includes step size.
# so basically u add another character indicating the interval
for number in range(1,10,3):
  print(number)   # output = 1,4,7


# Adding numbers in the range of 1-100
total = 0
for number in range(1,101):
  total += number
print(total)
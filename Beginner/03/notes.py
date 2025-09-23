# Think about your bathtub, ever wondered why it doesn't overflow?
# because you have a overflow point in the tub that drains the water so
# that there isnt any overflow of water

# Here in this case a condition is applied and thats the level of the water
# similarly in python conditional statements are if/else

# if condition:
#   do this
# else
#   do this

water_level = 50

if water_level>80:
    print("Drain Water")
else:
    print("Continue Water")

# think how this would apply in a rollercoaster height checker
# build the logic with the help of flowcharts and stuff

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:  # : is important for the conditional statements
    print("You're free to enter the rollercoaster!")
else:
    print("No rollercoaster for you!")


# MODULO OPERATOR %
# gives out the reminder of two numbers
# NO its not the percentage symbol

print(10/5) # here its dividing so 2
print(10%5) # output is 0
print(10%3) # 10/3 is 3.333333 and the modulo of these two is 1 cus 10 doesnt divide compeltely


# Nested If/ Else

# if condition:
#   if another_condition:
#      do this
#   else:
#      do this
# else:
#    do this

# as per the data and checks the programs written, the computer decides if
# it has to go inside the if condition or simply with else.


# this is all good but things can get more complex,
# like if the age is less than 12 u pay $5, 12-18 pays $7, above 18 pays $15

# thats why you hvae the ELIF statements

condition_is = 5

if condition_is == 5: # if condition one is true do that 
    print("Condition is true")
elif condition_is == 3: # but if thats not true then u can go down and do this
    print("condition is 3")
elif condition_is == 2:
    print("Condition is 2")
else: # this occurs when none of those are true.
    print("condition is whatevr")


# You use multiple ifs when checking for multiple statements being true/false
# even if previous statement is already true

# MULTIPLE IF

# if condition1:
#    do A
#  if condition2:
#    do B
#  if condition3:
#    do C


# WHICH/ONE??

# the choice of multiple ifs or if elifs depends on whether the conditions are mutually exclusive or if they can be true simulatinously

# use if, if multiple conditions can be true, and you want to execute code for each true condition. if statements below that will still
# run regardless of if the previous if statement is true

# so opposite of that use elifs if the conditions are mutually exclusive, if the if is true then everythign else is skipped.



# Logical Operators
# AND, or, not
# this is useful because you can combine two different conditions to one code.
# no notes for these should make sense beased on just experimentation

# AND = TRUE and TRUE = TRUE
#       TRUE and FALSE = FALSE
#       FALSE and FALSE = FALSE

# or, use this if you want just one thing to be true or false

# not: reversed true to false and false to true.

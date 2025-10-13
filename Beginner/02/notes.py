print(len("true"))

# what if I want to caluclate the len in input. If we run 
# print(len(1245)), we get a data type error.


# DATA TYPES

# "HELLO" == string

"Hello"[0] # we can access any position in a string, output = H, this is called SUBSCRIPTING
#01234

# 123 is not the same as "123"
print("123"+"345")
# INTEGERS
print(123 +345)
print(123456)
print(12_34_45) # _ is getting ignored

# FLOAT: has decimal points
print(3.35234)

# BOOLEAN: Only two values, true/false
True
False

# -------------------------------------------------------------------------------------------------------------------------------------

# TYPE ERROR, TYPE CHECKING AND TYPE CONVERSION

# To check data type:
print(type("hello"))
print(type(True))
print(type(123))
print(type(234.3))


# "123" this is a string right now

print("123"+"456")

#converting the string to int
print(int("123")+int("456"))

#but u cant always convert something to another data type

# print(int("abc")+int("def"))   This gives a value error


print("Number of letters in your name: " , len(input("Enter your name")))
# we're not using + because one part is a string and the other is an int

#Round

bmi = 84/1.65 **2
print(bmi)
print(round(bmi))

# reassigning values

score = 0
score -= 3
print(score)

# f strings: Used for mixing strings with data types

print(f"Hello, you scored {score} points, your bmi is {int(bmi)}")
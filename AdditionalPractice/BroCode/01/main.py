import math

'''
first_name = "Lekish"
print(first_name)


# Strings

first_name = "Lekish"
food = "pizza"
email = "broewey8r@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is{email}")


# Integers

age = 68
quantity = 3
num_of_students = 60
print(f"You are {age} years old")

# Floats

gpa = 4.3
price = 6.568
print(f"You gpa is {gpa}")

# Boolean

is_student = True
print(f"Are you a student?:{is_student}")


name = "Smith"
age = 28
gpa = 3.2
is_student = True

print(gpa)
gpa = int(gpa)
print(gpa)

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")



x = 3.14
y = 4
z = 5

result = round(x)
print(result)

result2 = abs(y)
print(result2)

result3 = pow(4, 3)
print(result3)

result4 = max(3,4,5)
print(result4)


print(math.pi)
print(math.e)

print(math.sqrt(57))
print(math.ceil(66))



radius = float(input("Enter the radius of your circle: "))
circum= 2 * math.pi * radius
area = math.pi * pow(radius,2)
print(f"The circumferance of your circle is {round(circum, 2)} cm")
print(f"The area of the circle is {round(area,2)}cm")

a = float(input("Enter side A length: "))
b = float(input("Enter side B length: "))

pythagorous = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(f"Side C length is: {round(pythagorous,2)}")

'''


age = int(input("Enter your age: "))

if age>=100:
  print("Boi you too old to sign up")
elif age >= 18:
  print("You are signed up")
elif age<0:
  print("You havent been born yet!")
else:
  print("You must be 18+ to sign up")



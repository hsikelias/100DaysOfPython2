# PYTHON NOTES

-----
**Date:** 10/30/25
**Topics:** 


**Variable**: A container for a value (string,integerm float, boolean). A variable behaves as if it was the value it contains.

```
first_name = "Lekish"
print(first_name)
```

- f-strings: We can use this to display our variable along with some texts.
```
first_name = "Lekish"
print(f"Hello {first_name}")
```

These are strings, strings CAN have numbers but they can't perform the usual arithmetic operations like real numbers do. Anything inside a " " are considered as strings.
```
first_name = "Lekish"
food = "pizza"
email = "broew568r@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is{email}")
```

Integers: 
```
age = 68
quantity = 3
num_of_students = 60
print(f"You are {age} years old")
```

Floats/Floating point numbers: Numbers with decimal portions, used for things like money

```
price = 6.568
```

Boolean: Consists of only True/False.. Used to make decisions 

is_student = True
print(f"Are you a student?:{is_student}")



**TypeCasting**
The process of converting a variable from one data type to another. str(), int(), float(), bool()

  - You can check the type of a variable through the **type** function
    ```
    num = 5
    print(type(num))
    ```
  - Converting an int to string
    ```
    print(gpa)  \\ gpa = 3.2
    gpa = int(gpa)
    print(gpa)  \\ gpa = 3
    ```
  - String to int is NOT possible


**User Input:** A function that prompts the user to enter data, returns the entered data as a string(It can be manipulated to a float/int/bool).

```
test = input("Enter your test information")
```

**Arithmetic Operators** 

Basic Arithmetic operators: 
```
friends += 1 \\ same as friends = friends + 1
friends -= 2 \\ same as friends = friends -2
friends *= 3 \\ friends = friends * 3
```
The first version is the **augmented** version,

- Exponents
  - friends = friends ** 2  or friends **= 2


Modulous(gives the remainder of any division). This is a very common operator used to find the even and odd number.
```
remainder = friends % 3
```

**Built in math functions**

1. Round: rounds a decimal number to an integer.
```
x = 3.14v

result = round(x)
print(result) //Output = 3
```
In round you can also add a parameter to describe how much u want the decimal to be rounded to. 

```
circum= 2 * math.pi * radius
print(f"The circumferance of your circle is {round(circum, 2)} cm")
```

2. Absolute: Converts a negative number to positive.
```
y = -5
result2 = abs(y)
print(result2) //Output = 5
```

3. Power: This is a built in function used to calculate the power of a number. It can be used in two or three argument forms. 

  4 is the base and 3 is the exponent so the output would be 64. 
```
result3 = pow(4, 3)
print(result3)
```

4. Max/Min: This is a built in function used to find the max number in the given variable/list and it prints out the highest one.

```
result4 = max(3,4,5)
print(result4) //Output = 5
```

```
result4 = max(3,4,5)
print(result4)  //Output = 3
```


Python offers some other various functions and constants but it requires us to import the module. which is ``import math``.


- ``print(math.pi)`` prints out the pi value
- ``print(math.e)`` prints out the e 
- ``print(math.sqrt(x))`` Finds the square root of the number x
- ``print(math.ceil(x))``  Ceiling function will always round a floating number up. So if our x is 66.06 or 66.96 it gives out the value as 67 no matter what.
- ``print(math.floor(x))`` Like ceil but instead of increasing a float number it decreases it



**If Statements**: When a code runs only IF some condition is True or else the program does something else. 

```
age = int(input("Enter your age: "))

if age >= 18:
  print("You are signed up")
else:
  print("You must be 18+ to sign up")

```
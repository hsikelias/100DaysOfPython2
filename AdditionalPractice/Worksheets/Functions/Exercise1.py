# Even or Odd function: takes in a number and then determines if the number is even or odd 
"""
def is_even_or_odd(number):
  if number % 2 == 0:
    print("Your number is even!")
  else:
    print("Your number is odd!")


print("Enter a number and we will determine if its an odd or even.")
is_even_or_odd(int(input("Enter a number: ")))
"""

"""
def sum_range(a, b):
  if a > b:
    sumRangeValue = 0
    #a, b = b, a
    print(sumRangeValue)
  return sum(range(a,b+1))


print("Sum Range Calculator")
A = int(input("Enter first value: "))
B = int(input("Enter second value: "))

print(sum_range(A,B))

"""
"""
def sum_digital (digit):
  sum_digits = 0
  for n in str(digit):
    sum_digits += int(n)
  return sum_digits

print("Enter a multiple digit number to find its sum!")
num = int(input("Enter a digit: "))
print(f"Sum of your number is: {sum_digital(num)}")


# n = 123
# need to create a variable that loops thru

"""

"""
def factorial(n):
  num_str = ""
  answer = 1
  for num in range(n):
    num_str += str((num + 1))
  num_list = [int(digit) for digit in str(num_str)]

  for num2 in num_list:
    answer *= num2
  return answer

print("Enter a number to find its factorial: \n")
num = int(input())
print(f"Factorial of your number is {factorial(num)}")
"""

def palindorme(word):
  word_as_list = word.split()
  print(word_as_list)
  # word_as_list_reversed = word_as_list.reverse()
  # print(word_as_list_reversed)

word = input("Enter the word you want to check if it reads the same backwards: ").lower()
print(f"Your word backwards is {palindorme(word)}")

"""
racecar
0123456

6543210

i basically need to reverse this list
"""
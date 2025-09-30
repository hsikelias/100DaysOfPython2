import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many symbols would you like?\n"))
nr_symbols = int(input("How many numbers would you like?\n"))


password = []

password_letters = random.choices(letters, k=nr_letters)
# the k parameter sepcifies the number of elements to select from a given sequence.
password_numbers = random.choices(numbers,k=nr_numbers)
password_symbols = random.choices(numbers,k=nr_symbols)


print(password_numbers)
print(password_letters)
print(password_symbols)

password_list = password_letters + password_numbers + password_symbols
random.shuffle(password_list)
print(password_list)

final_password = "".join(password_list)
print(f"Your password generated is: {final_password}")




# UDEMY COURSE METHOD: 

for char in range(0, nr_letters):
  # loop iterates over and over again in a list with for loop
  password.append(random.choice(letters))


for char in range(0, nr_symbols):
  password.append(random.choice(symbols))

for char in range(0, nr_numbers):
  password.append(random.choice(numbers))


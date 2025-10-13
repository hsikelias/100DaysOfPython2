import random

random_0to1 = random.randint(0,1)

print("Flip The coin!")
print("The coin faces on.....")
print("3....2....1")
if random_0to1 == 0:
    print("Heads!!")
else:
    print("Tails!!")
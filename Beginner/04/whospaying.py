import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

whospay = random.randint(0,4)
print(f"{friends[whospay]} will pay the bill!")

# above one is method one, we can also use random.choice()
print(random.choice(friends))

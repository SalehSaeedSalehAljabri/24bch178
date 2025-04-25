import random
random_numbers = random.sample(range(-15, 16), 10)
squares = list(map(lambda x: x**2, random_numbers))
print(random_numbers)
print(squares)

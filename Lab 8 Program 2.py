import random
random_numbers = {random.randint(15, 45) for _ in range(10)}
less_than_30_count = sum(1 for num in random_numbers if num < 30)
random_numbers = {num for num in random_numbers if num <= 35}
print("Random Numbers Set:", random_numbers)
print("Count of numbers less than 30:", less_than_30_count)

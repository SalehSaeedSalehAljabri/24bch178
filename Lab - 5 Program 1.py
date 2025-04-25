import random

odd_numbers = random.sample(range(1, 100, 2), 5)
print("Step 1: List of 5 random odd integers:")
print(odd_numbers)
even_numbers = random.sample(range(2, 100, 2), 4)
print("\nStep 2: List of 4 random even integers:")
print(even_numbers)
odd_numbers[2] = even_numbers
print("\nStep 3: Replacing 3rd element of odd list with even list:")
print(odd_numbers)
flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("\nStep 4: Flattened list:")
print(flattened_list)
sorted_list = sorted(flattened_list)
print("\nStep 5: Sorted list:")
print(sorted_list)

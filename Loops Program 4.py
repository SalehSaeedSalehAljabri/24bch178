def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is: {fact}")
    print("\n")
def pythagorean_triplets(limit):
    print(f"Pythagorean triplets with side lengths <= {limit} are:")
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    for triplet in triplets:
        print(triplet)
    print("\n")
num = int(input("Enter a number to calculate its factorial: "))
limit = int(input("Enter the maximum side length for Pythagorean triplets: "))
factorial(num)
pythagorean_triplets(limit)

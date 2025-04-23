# Program 8, 9, 10
import math

def print_natural_numbers_reverse(N):
    print(f"The first {N} natural numbers in reverse order are:")
    for i in range(N, 0, -1):
        print(i, end=' ')
    print("\n")
def fibonacci_series(N):
    print(f"The first {N} numbers in the Fibonacci series are:")
    fib = [0, 1]
    while len(fib) < N:
        fib.append(fib[-1] + fib[-2])
    print(fib[:N])
    print("\n")
def calculate_sine(x):
    sin_value = math.sin(x)
    print(f"The sine of {x} radians is: {sin_value}")
    print("\n")
N = int(input("Enter the value of N: "))
x = float(input("Enter the value of x (in radians) to calculate sin(x): "))
print_natural_numbers_reverse(N)
fibonacci_series(N)
calculate_sine(x)

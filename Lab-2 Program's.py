#Print largest and smallest values out of two.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
    print("Smallest:", b)
elif b > a:
    print("Largest:", b)
    print("Smallest:", a)
else:
    print("Both numbers are equal:", a)


#Print largest and smallest values out of three.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c
print("Largest number:", largest)
print("Smallest number:", smallest)


#Check whether a given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


#Check whether a given number is divisible by 10 or not.
num = int(input("Enter a number: "))
if num % 10 == 0:
    print(num, "is divisible by 10")
else:
    print(num, "is not divisible by 10")


#Accept age of a person. If age is less than 18, print minor otherwise Major.
age = int(input("Enter age: "))
if age < 18:
    print("Minor")
else:
    print("Major")


#Accept a number from the user. And print number of digits in it.
num = input("Enter a number: ")
if num[0] == '-':
    num = num[1:]
print("Number of digits:", len(num))

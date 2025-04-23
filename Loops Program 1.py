#Program 1
print("Uppercase letters:")
for ch in range(ord('A'), ord('Z') + 1):
    print(chr(ch), end=' ')
print("\n")
print("Lowercase letters:")
for ch in range(ord('a'), ord('z') + 1):
    print(chr(ch), end=' ')
print("\n")

#Program 2
num = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

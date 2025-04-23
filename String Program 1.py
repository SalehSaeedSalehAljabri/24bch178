A=input("Enter a string:")
vowels = "aeiouAEIOU"
vowelcount = 0
for char in A:
    if char in vowels:
        vowelcount+=1
print("Number of vowels:",vowelcount)

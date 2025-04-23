str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
if str2 in str1:
    print(f'"{str2}" is found in "{str1}"')
elif str1 in str2:
    print(f'"{str1}" is found in "{str2}"')
else:
    print("Neither string is present in the other.")

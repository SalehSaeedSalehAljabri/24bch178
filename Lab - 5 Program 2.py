import random

L=[]
for i in range (20):
    a=random.randint(1,100)
    L.append(a)
print(L)
B=int(input("Enter the number you want to search:"))
if B in L:
    print(L.index(B))
else:
    print("Number not found")

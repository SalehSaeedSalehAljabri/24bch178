f=open("Program 1.txt", mode="r")
print(f.read())  #For resding the elements in the text document.
f.close()

f1=open("Program1@1.txt", mode="w")  #W : for writing into the text document.
f1.write("Pandit Deenadayal Energy University.")
f1.close()  #Close the variable when its use is over.

f2=open("Program 1.txt", mode="a")
#print(f2.read())
f2.write("Date : 02/04/2025.")
f2.close()

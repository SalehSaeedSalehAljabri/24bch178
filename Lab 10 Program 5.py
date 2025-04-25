with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read().upper())
print("File copied and converted to uppercase successfully.")

with open("input.txt", "r") as src, open("output.txt", "w") as dest:
    text = src.read()
    for word in ["a", "the", "an"]:
        text = text.replace(f" {word} ", " ")
    dest.write(text)
print("Words removed successfully.")

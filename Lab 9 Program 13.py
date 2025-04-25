faculty_names = ["Christopher", "Alice", "Jonathan", "Bob", "Elizabeth"]
long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print(long_names)

names = [("John",), "Alice", ("Mike",), "Sophia", ("Jake",)]
boys = sum(1 for name in names if isinstance(name, tuple))
girls = len(names) - boys
print("Number of boys:", boys, "Number of girls:", girls)

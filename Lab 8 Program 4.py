names_set = {"Alice", "Bob", "Amanda", "Brian", "Andrew", "Betty"}
names_starting_with_a = {name for name in names_set if name.startswith("A")}
names_starting_with_b = {name for name in names_set if name.startswith("B")}
print("Names starting with A:", names_starting_with_a)
print("Names starting with B:", names_starting_with_b)

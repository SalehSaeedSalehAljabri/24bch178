def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])
print(reverse_list([1, 2, 3, 4, 5]))

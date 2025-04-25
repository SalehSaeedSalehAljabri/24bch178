def sanitize_list(lst):
    if not lst:
        return []
    return [max(0, lst[0])] + sanitize_list(lst[1:])
print(sanitize_list([-1, 2, -3, 4]))

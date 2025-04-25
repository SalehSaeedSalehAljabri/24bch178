def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)
print(to_binary(10))

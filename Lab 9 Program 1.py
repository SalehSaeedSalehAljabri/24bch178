def prime_factors(n, factor=2):
    if factor > n:
        return []
    if n % factor == 0:
        return [factor] + prime_factors(n // factor, factor)
    return prime_factors(n, factor + 1)
print(prime_factors(56))

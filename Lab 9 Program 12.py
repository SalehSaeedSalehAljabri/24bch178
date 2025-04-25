lst = ['madam', 'Python', 'malayalam', '12321']
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], lst))
print(palindromes)

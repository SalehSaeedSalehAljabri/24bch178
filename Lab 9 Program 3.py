def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0] in "aeiouAEIOU" else 0) + count_vowels(s[1:])
print(count_vowels("hello world"))


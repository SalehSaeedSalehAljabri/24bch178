def to_lower_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
def to_upper_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
def toggle_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
user_input = input("Enter a string:")
print("Lower case:", to_lower_case(user_input))
print("Upper case:", to_upper_case(user_input))
print("Toggle case:", toggle_case(user_input))

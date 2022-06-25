def double_char(string):
    doubled = ""
    for letter in range(len(string)):
        doubled += string[letter] * 2
    return doubled
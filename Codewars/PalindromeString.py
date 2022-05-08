def is_palindrome_sentence(string):
    i = ['!','?',',','.',' ','(', ')']
    for x in string:
        if x in i:
            string = string.replace(x, '')
    if string.lower() == string[::-1].lower():
        return True
    return False
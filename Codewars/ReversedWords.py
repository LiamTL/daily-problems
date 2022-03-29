# Complete the solution so that it reverses all of the words within the string passed in.

def reverseWords(str):
    new_arr = []
    for word in str.split():
        new_arr.append(word)
    new_arr.reverse()   
    return ' '.join(new_arr)
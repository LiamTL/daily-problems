# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

def find_missing_letter(chars):
    alphabet_com_and_cap = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    match = False
    count = 0
    for letter in alphabet_com_and_cap:
        if letter == chars[count]:
            match = True
            count += 1
            
        elif match == True:
            return letter
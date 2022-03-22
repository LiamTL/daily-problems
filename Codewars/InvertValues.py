# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negative, and the negative become positive.

def invert(lst):
    inv_list = []
    for num in lst:
        inv_list.append(num*-1)
    
    return inv_list
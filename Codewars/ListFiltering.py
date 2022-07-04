# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(lst):
    filtered_lst = []
    for elem in lst:
        if isinstance(elem, int):
            filtered_lst.append(elem)
    return filtered_lst
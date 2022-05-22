def find_it(lst):
    for odd_int in lst:
        if lst.count(odd_int) % 2 != 0:
            return odd_int
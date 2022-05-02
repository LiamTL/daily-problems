# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    product = 1
    for integer in arr:
        product = product * integer
    return product
# Complete the function that takes a non-negative integer n as input returns a list of all the powers of 2 with the exponent ranging from 0 to n.

def powers_of_two(n):
    powers_lst = []
    for power in range(0, n + 1):
        powers_lst.append(2 ** power)
    return powers_lst
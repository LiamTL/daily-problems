# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    if num == 1:
        return 1
    return num + summation(num - 1)
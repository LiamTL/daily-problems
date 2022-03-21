# Given an array of integers, return a new array with each value doubled.

def maps(arr):
    if len(arr) == 0:
        return []
    for num in range(len(arr)):
        arr[num] = arr[num] * 2
    return arr
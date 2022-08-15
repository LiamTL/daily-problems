# Given an array of integers, return a new array with each value doubled.

def maps(arr):
    for idx in range(len(arr)):
        arr[idx] = arr[idx] * 2
    return arr
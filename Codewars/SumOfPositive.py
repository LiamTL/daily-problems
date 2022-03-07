# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            result += arr[i]
    return result

# Codewars
# You get an array of numbers, return the sum of all of the positives ones.

# My psuedocode
# create a variable to store the sum
# loop through the array
#   add the current element to the sum
# return the sum

def positive_sum(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            result += arr[i]
    return result
